# Generated by Django 4.1 on 2022-08-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarjeta',
            name='id',
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='numero',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]