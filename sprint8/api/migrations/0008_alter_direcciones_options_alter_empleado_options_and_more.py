# Generated by Django 4.1 on 2022-08-30 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_direcciones_mtarjetas_tclien_tcuenta_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='direcciones',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='mtarjetas',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='sucursal',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tarjeta',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tclien',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tcuenta',
            options={'managed': True},
        ),
    ]
