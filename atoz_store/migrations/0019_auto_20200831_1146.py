# Generated by Django 3.0.3 on 2020-08-31 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atoz_store', '0018_manager_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discription',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('/pcs', '/peice'), ('/kgs', '/kgs')], max_length=30, null=True),
        ),
    ]
