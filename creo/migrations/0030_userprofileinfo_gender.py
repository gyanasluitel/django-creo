# Generated by Django 2.1.2 on 2019-01-04 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creo', '0029_auto_20190103_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=128),
        ),
    ]
