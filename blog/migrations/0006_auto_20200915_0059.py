# Generated by Django 3.1.1 on 2020-09-14 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200915_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topics',
            field=models.ManyToManyField(max_length=5, to='blog.Topic'),
        ),
    ]