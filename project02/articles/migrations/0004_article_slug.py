# Generated by Django 4.2.2 on 2023-07-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_created_at_article_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]