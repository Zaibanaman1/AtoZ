# Generated by Django 3.0.3 on 2020-08-02 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atoz_store', '0004_delete_extendeduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='something',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]