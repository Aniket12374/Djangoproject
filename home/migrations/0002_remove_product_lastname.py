# Generated by Django 5.0.7 on 2024-07-19 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='lastname',
        ),
    ]
