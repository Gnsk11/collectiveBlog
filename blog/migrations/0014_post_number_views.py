# Generated by Django 3.1.1 on 2020-09-15 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number_views',
            field=models.IntegerField(default=0),
        ),
    ]
