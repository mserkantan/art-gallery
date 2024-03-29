# Generated by Django 3.0.6 on 2020-05-25 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artifact_title', models.CharField(max_length=50)),
                ('artifact_original_title', models.CharField(max_length=50)),
                ('artifact_description', models.TextField()),
                ('artifact_creation', models.DateField()),
            ],
        ),
    ]
