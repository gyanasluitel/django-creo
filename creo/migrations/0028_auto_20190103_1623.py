# Generated by Django 2.1.2 on 2019-01-03 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creo', '0027_remove_postsubmission_content2'),
    ]

    operations = [
        migrations.AddField(
            model_name='postsubmission',
            name='audio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='postsubmission',
            name='image',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='postsubmission',
            name='video',
            field=models.BooleanField(default=False),
        ),
    ]
