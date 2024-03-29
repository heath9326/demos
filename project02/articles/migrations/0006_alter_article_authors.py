# Generated by Django 4.2.2 on 2023-07-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_author_user'),
        ('articles', '0005_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(related_name='articles', to='authors.author'),
        ),
    ]
