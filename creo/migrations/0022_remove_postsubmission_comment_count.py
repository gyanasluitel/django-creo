# Generated by Django 2.1.2 on 2018-12-27 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creo', '0021_postsubmission_comment_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postsubmission',
            name='comment_count',
        ),
    ]
