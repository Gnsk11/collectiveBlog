# Generated by Django 3.1.1 on 2020-09-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='posts',
            field=models.ManyToManyField(blank=True, to='blog.Post'),
        ),
    ]
