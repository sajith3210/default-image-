# Generated by Django 3.1.5 on 2022-02-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('countrty', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]