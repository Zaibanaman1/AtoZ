# Generated by Django 3.0.3 on 2020-08-02 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atoz_store', '0002_extendeduser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser',
            name='user',
        ),
    ]
