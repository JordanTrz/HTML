# Generated by Django 3.2 on 2022-02-05 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('url', models.CharField(max_length=200, verbose_name='URL')),
                ('fecha_registro', models.DateTimeField(null=True, verbose_name='Fecha de Registro')),
            ],
        ),
    ]