# Generated by Django 5.1.2 on 2024-10-10 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_genero', models.CharField(max_length=50)),
            ],
        ),
    ]
