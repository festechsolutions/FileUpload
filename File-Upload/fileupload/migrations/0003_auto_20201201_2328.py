# Generated by Django 3.1.3 on 2020-12-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0002_auto_20201201_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filesupload',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='filesupload',
            name='lname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='filesupload',
            name='phonenumber',
            field=models.IntegerField(null=True),
        ),
    ]
