# Generated by Django 3.0.2 on 2020-03-17 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0016_usergroup_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.CharField(max_length=31, primary_key=True, serialize=False)),
                ('chatinfo', models.CharField(max_length=20000)),
                ('shopid', models.CharField(max_length=30)),
                ('user1', models.CharField(max_length=50)),
                ('user2', models.CharField(max_length=50)),
                ('name1', models.CharField(max_length=50)),
                ('name2', models.CharField(max_length=50)),
            ],
        ),
    ]
