# Generated by Django 4.2.5 on 2023-09-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orderup", "0016_remove_customer_phone_number_customer_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="item_images"),
        ),
    ]
