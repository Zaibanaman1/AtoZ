# Generated by Django 3.0.3 on 2020-08-02 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('email', models.CharField(max_length=128, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Orderm', models.CharField(max_length=1000, null=True)),
                ('namem', models.CharField(max_length=400, null=True)),
                ('phonem', models.CharField(max_length=400, null=True)),
                ('trans_id', models.CharField(max_length=400, null=True)),
                ('productm', models.CharField(max_length=400, null=True)),
                ('quantitym', models.CharField(max_length=400, null=True)),
                ('adressm', models.CharField(max_length=400, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('totalm', models.CharField(max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('mark', models.IntegerField(default=1)),
                ('complete', models.BooleanField(default=True, null=True)),
                ('transaction_id', models.CharField(max_length=128, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atoz_store.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('prodtype', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=400, null=True)),
                ('city', models.CharField(max_length=400, null=True)),
                ('landmark', models.CharField(max_length=400, null=True)),
                ('phonenumber', models.IntegerField(default=404)),
                ('zipcode', models.CharField(max_length=400, null=True)),
                ('Order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atoz_store.Order')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atoz_store.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=7, null=True)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atoz_store.Order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atoz_store.Product')),
            ],
        ),
    ]
