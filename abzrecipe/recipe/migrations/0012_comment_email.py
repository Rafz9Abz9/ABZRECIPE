# Generated by Django 4.2.7 on 2023-11-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0011_comment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]