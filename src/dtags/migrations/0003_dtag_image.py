# Generated by Django 2.0.1 on 2018-01-21 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtags', '0002_auto_20180120_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='dtag',
            name='image',
            field=models.ImageField(default='img/default.jpeg', upload_to='img/{{ barcode_id }}/'),
        ),
    ]
