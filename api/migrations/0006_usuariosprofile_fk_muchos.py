# Generated by Django 5.1.2 on 2024-10-10 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_usuariosprofile_fk_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariosprofile',
            name='fk_muchos',
            field=models.ManyToManyField(to='api.generos'),
        ),
    ]
