# Generated by Django 5.0.4 on 2024-04-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
                ('image_name', models.TextField(null=True)),
                ('result', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
