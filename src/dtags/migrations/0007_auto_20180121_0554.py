# Generated by Django 2.0.1 on 2018-01-21 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtags', '0006_auto_20180121_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtag',
            name='image',
            field=models.ImageField(default='media/None/default.jpeg', upload_to='media/'),
        ),
    ]
