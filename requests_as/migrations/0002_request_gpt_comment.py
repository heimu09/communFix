# Generated by Django 4.1.7 on 2023-03-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests_as', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='gpt_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
