# Generated by Django 2.1.1 on 2019-02-10 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20190209_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='researchers',
        ),
        migrations.AddField(
            model_name='project',
            name='researchers',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
