# Generated by Django 3.0.2 on 2020-03-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0020_delete_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='productid',
            field=models.CharField(max_length=30),
        ),
    ]
