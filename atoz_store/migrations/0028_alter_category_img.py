# Generated by Django 3.2.2 on 2021-10-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atoz_store', '0027_auto_20211024_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]