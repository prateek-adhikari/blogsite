# Generated by Django 2.1 on 2020-04-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
    ]
