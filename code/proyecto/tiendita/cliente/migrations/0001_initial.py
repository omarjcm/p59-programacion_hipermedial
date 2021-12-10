# Generated by Django 3.2.9 on 2021-12-10 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('correo_electronico', models.EmailField(max_length=254)),
            ],
        ),
    ]
