# Generated by Django 5.0.1 on 2024-01-31 15:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('hsc_roll', models.CharField(max_length=10, null=True, unique=True)),
                ('hsc_reg', models.CharField(max_length=16, null=True, unique=True)),
                ('reg_no', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('roll', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('session', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('fathers_name', models.CharField(max_length=30, null=True)),
                ('mothers_name', models.CharField(max_length=30, null=True)),
                ('guardian_phone', models.CharField(max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=3000, null=True)),
                ('CGPA', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('result_description', models.CharField(blank=True, default='No Details Available now.', max_length=3000, null=True)),
            ],
        ),
    ]
