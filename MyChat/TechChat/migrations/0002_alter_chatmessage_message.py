# Generated by Django 4.2.13 on 2024-05-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechChat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='message',
            field=models.CharField(max_length=10000000),
        ),
    ]
