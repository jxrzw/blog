# Generated by Django 2.0 on 2019-05-08 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='icon',
            field=models.ImageField(default='uploads/mine1.png', upload_to='uploads/%Y/%m/%d'),
        ),
    ]
