# Generated by Django 5.0.1 on 2024-02-14 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_adminnotice_teacher'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdminNotice',
        ),
        migrations.RemoveField(
            model_name='student',
            name='dept',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
