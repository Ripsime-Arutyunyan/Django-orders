# Generated by Django 4.1.1 on 2022-09-28 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="item_name",
            field=models.CharField(default="item", max_length=100),
            preserve_default=False,
        ),
    ]
