# Generated by Django 3.2.25 on 2025-02-05 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_post_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
