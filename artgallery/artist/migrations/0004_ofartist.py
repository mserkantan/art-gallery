# Generated by Django 3.0.6 on 2020-05-26 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art_movement', '0002_auto_20200525_2226'),
        ('artist', '0003_auto_20200527_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_movement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='art_movement.Art_Movement')),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artist.Artist')),
            ],
        ),
    ]
