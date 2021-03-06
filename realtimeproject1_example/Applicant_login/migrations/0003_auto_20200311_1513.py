# Generated by Django 2.1 on 2020-03-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant_login', '0002_auto_20200310_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantFormModel',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('NAME', models.CharField(max_length=30, unique=True)),
                ('DATE_OF_BIRTH', models.DateField(help_text='yyyy-mm-dd')),
                ('GENDER', models.CharField(max_length=30)),
                ('MOBILE', models.IntegerField()),
                ('QUALIFICATION', models.CharField(max_length=30)),
                ('POST', models.FloatField()),
                ('PERCENTAGE', models.FloatField()),
                ('RESUME', models.FileField(upload_to='applicant_document')),
            ],
        ),
        migrations.AlterField(
            model_name='addingdetailsmodel',
            name='DATE_OF_BIRTH',
            field=models.DateField(help_text='yyyy-mm-dd'),
        ),
    ]
