# Generated by Django 4.2.9 on 2024-01-07 21:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carreviewmodel",
            name="hp",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        66, message="Invalid input, the value is too low"
                    ),
                    django.core.validators.MaxValueValidator(
                        2012, message="Invalid input, value to high"
                    ),
                ]
            ),
        ),
    ]
