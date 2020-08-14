# Generated by Django 3.0.3 on 2020-08-10 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atoz_store', '0016_auto_20200810_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('op', 'order processing'), ('od', 'out for delivery'), ('d', 'delivered')], default='null', max_length=40, null=True),
        ),
    ]