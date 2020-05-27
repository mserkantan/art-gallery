# Generated by Django 3.0.6 on 2020-05-26 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_auto_20200527_0146'),
        ('artist', '0002_auto_20200525_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='place_born',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='place_born', to='place.Place'),
        ),
        migrations.AddField(
            model_name='artist',
            name='place_death',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='place_death', to='place.Place'),
        ),
    ]
