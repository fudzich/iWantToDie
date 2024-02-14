# Generated by Django 5.0.1 on 2024-02-12 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pls_w', '0005_alter_gamegenre_genre_main_alter_gamegenre_genre_sub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(default='def', help_text="Enter game's genre", on_delete=django.db.models.deletion.CASCADE, to='pls_w.gamegenre', verbose_name='Genre'),
        ),
    ]
