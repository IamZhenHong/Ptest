# Generated by Django 4.2.5 on 2023-12-01 00:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trials", "0005_personalitytype_images_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="personalitytype",
            name="name_image_path",
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
