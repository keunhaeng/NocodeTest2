# Generated by Django 4.2.4 on 2023-08-04 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_rename_userpw_userdetail_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='phone',
            field=models.TextField(blank=True, default=0, max_length=11, null=True),
        ),
    ]
