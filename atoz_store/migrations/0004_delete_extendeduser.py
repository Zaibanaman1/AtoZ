# Generated by Django 3.0.3 on 2020-08-02 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atoz_store', '0003_remove_extendeduser_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='extendeduser',
        ),
    ]
