# Generated by Django 4.2.3 on 2023-07-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0006_alter_image_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create',
            name='picture',
        ),
        migrations.AddField(
            model_name='create',
            name='picture',
            field=models.ManyToManyField(to='posting.image'),
        ),
    ]