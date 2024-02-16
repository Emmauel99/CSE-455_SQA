# Generated by Django 4.1.3 on 2024-02-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default='Admin', max_length=30)),
                ('receiver', models.CharField(max_length=20, null=True)),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
