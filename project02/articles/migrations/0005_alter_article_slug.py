# Generated by Django 4.2.2 on 2023-07-21 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='slug', max_length=150),
        ),
    ]
