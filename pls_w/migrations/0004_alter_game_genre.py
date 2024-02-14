# Generated by Django 5.0.1 on 2024-02-12 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pls_w', '0003_gamegenre_genre_alter_game_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(blank=True, help_text="Enter game's genre", null=True, on_delete=django.db.models.deletion.CASCADE, to='pls_w.gamegenre', verbose_name='Genre'),
        ),
    ]