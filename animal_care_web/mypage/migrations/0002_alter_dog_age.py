# Generated by Django 5.0.4 on 2024-04-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mypage", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dog",
            name="age",
            field=models.PositiveIntegerField(),
        ),
    ]
