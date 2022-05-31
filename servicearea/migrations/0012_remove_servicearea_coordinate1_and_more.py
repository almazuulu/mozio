# Generated by Django 4.0.4 on 2022-05-31 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicearea', '0011_alter_servicearea_coordinate1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicearea',
            name='coordinate1',
        ),
        migrations.RemoveField(
            model_name='servicearea',
            name='coordinate2',
        ),
        migrations.RemoveField(
            model_name='servicearea',
            name='coordinate3',
        ),
        migrations.RemoveField(
            model_name='servicearea',
            name='coordinate4',
        ),
        migrations.AddField(
            model_name='servicearea',
            name='lat1',
            field=models.FloatField(blank=True, null=True, verbose_name='Latitude 1'),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='lat2',
            field=models.FloatField(blank=True, null=True, verbose_name='Latitude 2'),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='lat3',
            field=models.FloatField(blank=True, null=True, verbose_name='Latitude 3'),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='lat4',
            field=models.FloatField(blank=True, null=True, verbose_name='Latitude 4'),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='lon1',
            field=models.FloatField(blank=True, null=True, verbose_name='Longitude 1'),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='lon2',
            field=models.FloatField(blank=True, null=True, verbose_name='Longitude 2'),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='lon3',
            field=models.FloatField(blank=True, null=True, verbose_name='Longitude 3'),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='lon4',
            field=models.FloatField(blank=True, null=True, verbose_name='Longitude 4'),
        ),
    ]
