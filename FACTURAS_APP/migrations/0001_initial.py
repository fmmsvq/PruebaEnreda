# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='documents/')),
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
                ('iva', models.IntegerField()),
                ('contrato', models.ForeignKey(to='FACTURAS_APP.Contrato')),
            ],
        ),
        migrations.CreateModel(
            name='Liquidacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('publicada', models.BooleanField()),
                ('nombre', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='liquidacion',
            field=models.ForeignKey(to='FACTURAS_APP.Liquidacion'),
        ),
        migrations.AddField(
            model_name='factura',
            name='nombre',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contrato',
            name='liquidacion',
            field=models.ForeignKey(to='FACTURAS_APP.Liquidacion'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='nombre',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
