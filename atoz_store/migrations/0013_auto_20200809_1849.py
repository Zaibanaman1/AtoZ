# Generated by Django 3.0.3 on 2020-08-09 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atoz_store', '0012_auto_20200809_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='status',
            new_name='Status',
        ),
    ]
