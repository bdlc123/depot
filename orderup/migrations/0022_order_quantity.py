# Generated by Django 4.2.5 on 2023-09-21 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orderup", "0021_order_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
