# Generated by Django 3.0.6 on 2020-05-25 22:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20200525_2213'),
        ('art_object', '0002_artifactimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='artist_id',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='artist.Artist'),
        ),
    ]