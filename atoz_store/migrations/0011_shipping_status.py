# Generated by Django 3.0.3 on 2020-08-09 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atoz_store', '0010_auto_20200809_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='status',
            field=models.CharField(choices=[('orderprocessing', 'order processing'), ('outfordelivery', 'out for delivery'), ('delivered', 'delivered')], max_length=40, null=True),
        ),
    ]