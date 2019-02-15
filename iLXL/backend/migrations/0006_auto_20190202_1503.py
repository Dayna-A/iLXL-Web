# Generated by Django 2.1.1 on 2019-02-02 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20190202_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='internship_interest',
            new_name='internship_availability',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='newgrad_interest',
            new_name='newgrad_availability',
        ),
        migrations.AlterField(
            model_name='member',
            name='cs_interests',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='github_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='website_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]