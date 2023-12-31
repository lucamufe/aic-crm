# Generated by Django 4.2.3 on 2023-07-22 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostoProyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('fecha', models.DateField()),
                ('ubicacion', models.CharField(max_length=60)),
                ('categoria', models.CharField(max_length=60)),
                ('producto', models.CharField(max_length=60)),
                ('medida', models.CharField(max_length=60)),
                ('cantidad', models.DecimalField(decimal_places=1, max_digits=7)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('gastos', models.DecimalField(decimal_places=2, max_digits=8)),
                ('usuario', models.CharField(max_length=60)),
            ],
        ),
    ]
