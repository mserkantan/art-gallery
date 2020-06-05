# Generated by Django 3.0.6 on 2020-06-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200527_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_real_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_surname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
