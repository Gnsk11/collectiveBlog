# Generated by Django 3.1.1 on 2020-09-26 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_number_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('can_change_status', 'Can change post status')]},
        ),
    ]
