# Generated by Django 4.2.5 on 2023-09-18 19:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("orderup", "0010_alter_order_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="order_number",
            field=models.CharField(default="H6845-", max_length=20),
        ),
        migrations.AlterField(
            model_name="order",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                help_text="Unique ID for orders",
                primary_key=True,
                serialize=False,
            ),
        ),
    ]