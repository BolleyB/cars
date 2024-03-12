# Generated by Django 5.0.3 on 2024-03-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_car_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='engine',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='car',
            name='manufacture_date',
            field=models.DateField(default='1970-01-01'),
        ),
        migrations.AddField(
            model_name='car',
            name='predecessor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='successor',
            field=models.CharField(default='', max_length=100),
        ),
    ]
