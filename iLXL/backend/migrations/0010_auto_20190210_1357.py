# Generated by Django 2.1.1 on 2019-02-10 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20190210_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-when']},
        ),
        migrations.AlterModelOptions(
            name='grant',
            options={'ordering': ['-date_of_grant']},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-time_posted']},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['-date_of_publication']},
        ),
    ]
