# Generated by Django 2.1.2 on 2019-01-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creo', '0025_auto_20190103_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='postsubmission',
            name='content2',
            field=models.FileField(blank=True, upload_to='postedvideos'),
        ),
    ]
