# Generated by Django 5.1.2 on 2024-10-10 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_generos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generos',
            name='id',
            field=models.AutoField(db_column='genero_id', primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='generos',
            table='generos',
        ),
    ]