# Generated by Django 2.2.2 on 2020-10-20 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20201019_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='gols_desafiante',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='partida',
            name='gols_visitante',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]