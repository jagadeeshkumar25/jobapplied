# Generated by Django 2.1 on 2020-03-15 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interviewer_LoginModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USERNAME', models.CharField(max_length=30)),
                ('PASSWORD', models.CharField(max_length=30)),
            ],
        ),
    ]
