# Generated by Django 3.1.1 on 2020-09-14 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_date_time_posting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='post',
            name='topics',
        ),
    ]
