# Generated by Django 2.1.1 on 2019-02-02 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='newgrad_interest',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]