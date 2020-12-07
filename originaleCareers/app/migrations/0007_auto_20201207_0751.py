# Generated by Django 3.1.3 on 2020-12-07 02:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201207_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobtype',
            name='experince',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(21), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='jobtype',
            name='salary',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10000000), django.core.validators.MinValueValidator(1)]),
        ),
    ]