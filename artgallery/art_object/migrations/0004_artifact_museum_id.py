# Generated by Django 3.0.6 on 2020-05-26 22:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0001_initial'),
        ('art_object', '0003_artifact_artist_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='museum_id',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='museum.Museum'),
        ),
    ]
