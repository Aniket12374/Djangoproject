# Generated by Django 5.0.7 on 2024-07-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_orderitem_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductQuerySet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
