# Generated by Django 3.0.2 on 2020-01-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_usergroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergroup',
            name='id',
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='shopId',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]