# Generated by Django 3.0.2 on 2020-01-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_auto_20200113_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinfo',
            name='userName',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
