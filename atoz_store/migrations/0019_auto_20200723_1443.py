# Generated by Django 3.0.3 on 2020-07-23 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atoz_store', '0018_auto_20200722_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipping',
            old_name='state',
            new_name='landmark',
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atoz_store.Customer'),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atoz_store.Customer'),
        ),
    ]
