# Generated by Django 4.2.5 on 2023-09-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orderup", "0009_remove_order_order_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]