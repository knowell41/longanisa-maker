# Generated by Django 4.2.8 on 2023-12-27 05:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0008_remove_flavor_ingredient1_remove_flavor_ingredient2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuator',
            name='tie',
            field=models.CharField(default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]
