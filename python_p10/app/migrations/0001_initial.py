# Generated by Django 4.2.2 on 2023-07-06 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.CharField(max_length=36)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, default='')),
                ('priority',
                 models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], max_length=16)),
                ('type',
                 models.CharField(choices=[('BUG', 'Bug'), ('FEATURE', 'Feature'), ('TASK', 'Task')], max_length=16)),
                ('status',
                 models.CharField(choices=[('TODO', 'To Do'), ('PROGRESS', 'In Progress'), ('FINISHED', 'Finished')],
                                  default='TODO', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, default='')),
                ('type',
                 models.CharField(choices=[('BE', 'Back-End'), ('FE', 'Front-End'), ('IOS', 'IOS'), ('AD', 'Android')],
                                  max_length=16)),
            ],
        ),
    ]
