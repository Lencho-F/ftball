# Generated by Django 4.2.5 on 2023-09-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_userprofile_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]