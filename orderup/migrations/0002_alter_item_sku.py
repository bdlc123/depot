# Generated by Django 4.2.5 on 2023-09-18 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orderup", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item", name="SKU", field=models.IntegerField(),
        ),
    ]
