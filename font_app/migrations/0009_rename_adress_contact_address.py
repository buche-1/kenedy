# Generated by Django 3.2.12 on 2022-04-13 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('font_app', '0008_auto_20220413_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='adress',
            new_name='address',
        ),
    ]
