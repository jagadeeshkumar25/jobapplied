# Generated by Django 3.0 on 2020-02-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hradmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addemployeemodel',
            name='CONTACTNO',
            field=models.IntegerField(),
        ),
    ]