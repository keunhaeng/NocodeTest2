# Generated by Django 4.2.1 on 2023-08-02 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userdetail_userid_userdetail_userpw'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]
