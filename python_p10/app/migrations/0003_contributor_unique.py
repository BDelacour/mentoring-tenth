# Generated by Django 4.2.2 on 2023-07-06 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='contributor',
            constraint=models.UniqueConstraint(fields=('user', 'project'), name='unique'),
        ),
    ]