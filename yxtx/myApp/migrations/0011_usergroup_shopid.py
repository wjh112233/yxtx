# Generated by Django 3.0.2 on 2020-01-17 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_auto_20200117_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='shopId',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
