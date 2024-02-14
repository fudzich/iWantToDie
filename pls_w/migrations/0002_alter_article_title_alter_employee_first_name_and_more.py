# Generated by Django 5.0.1 on 2024-02-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pls_w', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text="Enter article's title", max_length=20, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(help_text='Enter your first name', max_length=20, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(help_text='Enter your last name', max_length=20, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(help_text='Enter your position', max_length=20, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(help_text="Enter game's genre", max_length=20, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(help_text="Enter game's title", max_length=20, verbose_name='Title'),
        ),
    ]
