# Generated by Django 4.2.8 on 2023-12-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0003_alter_flavor_amount1_alter_flavor_amount2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flavor',
            name='amount1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='amount2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='amount3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='amount4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='amount5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='ingredient1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='ingredient2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='ingredient3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='ingredient4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='ingredient5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
