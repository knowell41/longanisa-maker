from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .utils import ControlSystem
import time
import threading
from django.views.decorators.csrf import csrf_exempt

device_instance = DeviceSettings.objects.all().first()
device = ControlSystem()
try:
    device.com = device_instance.com
    device.baud = device_instance.baudrate
    device.timeout = device_instance.timeout
    device.connect()
    time.sleep(2)
except Exception as e:
    print(f"{e}")


class ResetSerial(APIView):
    global device

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        # try:
        try:
            device.close()
        except:
            pass
        for i in range(255):
            try:
                device.com = f"/dev/ttyACM{i}"
                device.connect()
                break
            except Exception as e:
                print(f"{e}")
                continue

        serial_info = {
            "port": device.serial_com.name,
            "baudrate": device.serial_com.baudrate,
            "timeout": device.serial_com.timeout,
        }
        return Response(serial_info, status=status.HTTP_200_OK)
        # except Exception as e:
        #     return Response({"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PingSerial(APIView):
    global device

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            device.connect()
            return Response("CONNECTED", status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response("DISCONNECTED", status=status.HTTP_200_OK)


class ListFlavors(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlavorSerializer
    queryset = Flavor.objects.all()

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        return super().get(request, args, kwargs)


class CreateFlavor(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlavorSerializer
    queryset = Flavor.objects.all()
    parser_classes = [MultiPartParser]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RetrieveFlavor(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlavorSerializer
    queryset = Flavor.objects.all()

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        return super().get(request, args, kwargs)


class DeleteFlavor(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlavorSerializer
    queryset = Flavor.objects.all()

    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        return super().get(request, args, kwargs)


class UpdateFlavor(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlavorSerializer
    queryset = Flavor.objects.all()
    http_method_names = ["patch"]

    @csrf_exempt
    def patch(self, request, *args, **kwargs):
        return super().get(request, args, kwargs)


class AppStatus(APIView):
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        try:
            app_status = AppSettings.objects.get(id=1)
            return Response(app_status.systemStatus, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class SetAppStatus(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    @csrf_exempt
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="status",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                description="Set status",
                enum=["START", "STOP"],
                required=False,
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            set_status = data.get("status")

            app_status = AppSettings.objects.get(id=1)

            if set_status == "START":
                app_status.systemStatus = "RUNNING"
                app_status.save()
                return Response("RUNNING", status=status.HTTP_200_OK)

            if set_status == "STOP":
                app_status.systemStatus = "STOPPED"
                app_status.save()
                return Response("STOPPED", status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class Dispense(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    flavors_queryset = Flavor.objects.all()
    flavor_list = []
    for flavor in flavors_queryset:
        flavor_list.append(flavor.title)

    @csrf_exempt
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="flavor",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                description="flavor",
                required=False,
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        try:
            flavor = request.data.get("flavor")
            self.run_system(flavor)
            return Response(flavor, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def convert(self, grams) -> float:
        return grams / 100

    def run_system(self, flavor):
        flavor_instance = Flavor.objects.get(title=flavor)
        actuator_instance = Actuator.objects.get(id=1)
        if device:
            amount1 = flavor_instance.amount1
            if amount1:
                condiment1 = actuator_instance.condiment1
                delay1 = self.convert(amount1)
                thread1 = threading.Thread(
                    target=self.dispense_condiment, args=(device, condiment1, delay1)
                )
                thread1.start()
            amount2 = flavor_instance.amount2
            if amount2:
                condiment2 = actuator_instance.condiment2
                delay2 = self.convert(amount2)
                thread2 = threading.Thread(
                    target=self.dispense_condiment, args=(device, condiment2, delay2)
                )
                thread2.start()
            amount3 = flavor_instance.amount3
            if amount3:
                condiment3 = actuator_instance.condiment3
                delay3 = self.convert(amount3)
                thread3 = threading.Thread(
                    target=self.dispense_condiment, args=(device, condiment3, delay3)
                )
                thread3.start()
            amount4 = flavor_instance.amount4
            if amount4:
                condiment4 = actuator_instance.condiment4
                delay4 = self.convert(amount4)
                thread4 = threading.Thread(
                    target=self.dispense_condiment, args=(device, condiment4, delay4)
                )
                thread4.start()
            amount5 = flavor_instance.amount5
            if amount5:
                condiment5 = actuator_instance.condiment5
                delay5 = self.convert(amount5)
                thread5 = threading.Thread(
                    target=self.dispense_condiment, args=(device, condiment5, delay5)
                )
                thread5.start()

            grinder1 = actuator_instance.grinder1
            device.on(pin=grinder1)
            grinder2 = actuator_instance.grinder2
            device.on(pin=grinder2)
            grinder3 = actuator_instance.grinder3
            device.on(pin=grinder3)
            grinder4 = actuator_instance.grinder4
            device.on(pin=grinder4)
            mixer = actuator_instance.mixer
            device.on(pin=mixer)

            thread1.join()
            thread2.join()
            thread3.join()
            thread4.join()
            thread5.join()

            grinder1 = actuator_instance.grinder1
            device.off(pin=grinder1)
            grinder2 = actuator_instance.grinder2
            device.off(pin=grinder2)
            grinder3 = actuator_instance.grinder3
            device.off(pin=grinder3)
            grinder4 = actuator_instance.grinder4
            device.off(pin=grinder4)

            for i in range(60):
                print(f"Mixing.... {i}", end="\r")
                time.sleep(1)

            mixer = actuator_instance.mixer
            device.off(pin=mixer)

            time.sleep(1)

            # device.close()

    def dispense_condiment(self, device, pin, delay):
        if device:
            device.dispense(delay=delay, pin=pin)
            time.sleep(1)


class Mixer(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    @csrf_exempt
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="action",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                description="action",
                enum=["ON", "OFF"],
                required=False,
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        try:
            if device:
                actuator_instance = Actuator.objects.get(id=1)
                data = request.data
                action = data.get("action")
                mixer = actuator_instance.mixer
                if action == "ON":
                    device.on(pin=mixer)
                    return Response("ON", status=status.HTTP_200_OK)

                if action == "OFF":
                    device.off(pin=mixer)
                    return Response("OFF", status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class Grinder(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    @csrf_exempt
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="action",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                description="action",
                enum=["ON", "OFF"],
                required=False,
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        try:
            if device:
                actuator_instance = Actuator.objects.get(id=1)
                data = request.data
                action = data.get("action")
                mixer = actuator_instance.mixer
                if action == "ON":
                    grinder1 = actuator_instance.grinder1
                    device.on(pin=grinder1)
                    # grinder2 = actuator_instance.grinder2
                    # device.on(pin=grinder2)
                    # grinder3 = actuator_instance.grinder3
                    # device.on(pin=grinder3)
                    # grinder4 = actuator_instance.grinder4
                    # device.on(pin=grinder4)
                    return Response("ON", status=status.HTTP_200_OK)

                if action == "OFF":
                    grinder1 = actuator_instance.grinder1
                    device.off(pin=grinder1)
                    # grinder2 = actuator_instance.grinder2
                    # device.off(pin=grinder2)
                    # grinder3 = actuator_instance.grinder3
                    # device.off(pin=grinder3)
                    # grinder4 = actuator_instance.grinder4
                    # device.off(pin=grinder4)
                    return Response("OFF", status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class Tie(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    @csrf_exempt
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="action",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                description="action",
                enum=["ON", "OFF"],
                required=False,
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        try:
            if device:
                actuator_instance = Actuator.objects.get(id=1)
                data = request.data
                action = data.get("action")
                tie = actuator_instance.tie
                if action == "ON":
                    device.on(tie)
                    return Response("ON", status=status.HTTP_200_OK)

                if action == "OFF":
                    device.off(tie)
                    return Response("OFF", status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
