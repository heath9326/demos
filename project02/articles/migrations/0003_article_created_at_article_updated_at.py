# Generated by Django 4.2.2 on 2023-07-21 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2023-07-18T09:00:20Z'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]