# Generated by Django 3.1.7 on 2021-03-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210313_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='city',
            field=models.CharField(default='', max_length=111),
        ),
    ]