# Generated by Django 3.1.1 on 2020-09-14 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200915_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_time_publication',
            field=models.DateTimeField(),
        ),
    ]
