# Generated by Django 4.2.8 on 2023-12-22 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0006_alter_devicesettings_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condiment1', models.CharField(max_length=2)),
                ('condiment2', models.CharField(max_length=2)),
                ('condiment3', models.CharField(max_length=2)),
                ('condiment4', models.CharField(max_length=2)),
                ('condiment5', models.CharField(max_length=2)),
                ('grinder1', models.CharField(max_length=2)),
                ('grinder2', models.CharField(max_length=2)),
                ('grinder3', models.CharField(max_length=2)),
                ('grinder4', models.CharField(max_length=2)),
                ('mixer', models.CharField(max_length=2)),
            ],
        ),
    ]
