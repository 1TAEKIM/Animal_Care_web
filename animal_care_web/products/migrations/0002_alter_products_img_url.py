# Generated by Django 5.0.4 on 2024-04-22 06:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="img_url",
            field=models.TextField(null=True),
        ),
    ]
