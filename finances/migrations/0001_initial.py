# Generated by Django 4.1.7 on 2023-03-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expenses', models.DecimalField(decimal_places=2, max_digits=10)),
                ('details', models.TextField()),
            ],
        ),
    ]
