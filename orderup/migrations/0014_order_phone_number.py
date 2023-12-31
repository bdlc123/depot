# Generated by Django 4.2.5 on 2023-09-19 16:13

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("orderup", "0013_rename_order_number_order_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, region=None
            ),
        ),
    ]
