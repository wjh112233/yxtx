# Generated by Django 3.0.2 on 2020-03-28 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0023_qualifiedteacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualifiedteacher',
            name='canCourse',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='qualifiedteacher',
            name='isexperience',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='qualifiedteacher',
            name='majorQualified',
            field=models.CharField(max_length=100),
        ),
    ]
