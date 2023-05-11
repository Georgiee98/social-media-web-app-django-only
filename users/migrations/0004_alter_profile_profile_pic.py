# Generated by Django 3.2.18 on 2023-05-11 17:50

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default=users.models.generate_default_profile_pic, upload_to='users/%d/%m/%Y'),
        ),
    ]
