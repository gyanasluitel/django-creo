# Generated by Django 2.1.2 on 2019-01-03 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creo', '0024_auto_20190103_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='like',
            field=models.BooleanField(),
        ),
    ]
