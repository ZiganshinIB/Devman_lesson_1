# Generated by Django 4.2.11 on 2024-04-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0006_alter_imageplace_options_imageplace_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageplace',
            name='position',
            field=models.PositiveIntegerField(default=0, verbose_name='Позиция'),
        ),
    ]
