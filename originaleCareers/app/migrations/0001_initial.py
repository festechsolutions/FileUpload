# Generated by Django 3.1.4 on 2020-12-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jt', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='userJobTp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100, null=True)),
                ('lname', models.CharField(max_length=100, null=True)),
                ('phonenumber', models.CharField(max_length=10, null=True)),
                ('emai', models.EmailField(max_length=100, null=True)),
                ('workex', models.IntegerField(null=True)),
                ('jobdes', models.CharField(max_length=1000, null=True)),
                ('resume', models.FileField(upload_to='')),
            ],
        ),
    ]