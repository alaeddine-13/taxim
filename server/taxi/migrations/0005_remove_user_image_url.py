# Generated by Django 3.1 on 2020-11-02 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0004_auto_20201102_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image_url',
        ),
    ]