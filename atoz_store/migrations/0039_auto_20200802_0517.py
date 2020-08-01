# Generated by Django 3.0.3 on 2020-08-01 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atoz_store', '0038_auto_20200802_0324'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='shipping',
            name='phonenumber',
            field=models.IntegerField(default=404),
        ),
        migrations.DeleteModel(
            name='extendeduser',
        ),
    ]
