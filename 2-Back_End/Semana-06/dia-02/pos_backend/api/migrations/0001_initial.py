# Generated by Django 3.2 on 2022-02-03 01:18

import cloudinary.models
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
            name='Categoria',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria_nom', models.CharField(max_length=100, verbose_name='nombre de categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('mesa_id', models.AutoField(primary_key=True, serialize=False)),
                ('mesa_nro', models.CharField(max_length=10, verbose_name='Nro Mesa')),
                ('mesa_cap', models.IntegerField(default=0, verbose_name='Capacidad')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('pedido_id', models.AutoField(primary_key=True, serialize=False)),
                ('pedido_fech', models.DateTimeField(null=True, verbose_name='Fecha')),
                ('pedido_nro', models.CharField(default='', max_length=100, verbose_name='Nro Pedido')),
                ('pedido_est', models.CharField(default='pagado', max_length=100, verbose_name='Estado')),
                ('mesa_id', models.ForeignKey(db_column='mesa_id', on_delete=django.db.models.deletion.RESTRICT, to='api.mesa', verbose_name='Mesa')),
                ('usu_id', models.ForeignKey(db_column='usu_id', on_delete=django.db.models.deletion.RESTRICT, related_name='Pedidos', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('plato_id', models.AutoField(primary_key=True, serialize=False)),
                ('plato_nom', models.CharField(max_length=200, verbose_name='nombre del plato')),
                ('plato_img', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image')),
                ('plato_pre', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='precio')),
                ('categoria_id', models.ForeignKey(db_column='categoria_id', on_delete=django.db.models.deletion.RESTRICT, related_name='Platos', to='api.categoria', verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoPlato',
            fields=[
                ('pedidoplato_id', models.AutoField(primary_key=True, serialize=False)),
                ('pedidoplato_cant', models.IntegerField(default=1)),
                ('pedido_id', models.ForeignKey(db_column='pedido_id', on_delete=django.db.models.deletion.RESTRICT, related_name='pedidoplatos', to='api.pedido', verbose_name='Pedido')),
                ('plato_id', models.ForeignKey(db_column='plato_id', on_delete=django.db.models.deletion.RESTRICT, related_name='pedidoplatos', to='api.plato', verbose_name='Plato')),
            ],
        ),
    ]
