# Generated by Django 5.0.4 on 2024-04-23 06:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_products_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("summary", models.TextField()),
                ("content", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("img_url", models.ImageField(upload_to="products/")),
                ("categories", models.ManyToManyField(to="products.category")),
            ],
        ),
    ]
