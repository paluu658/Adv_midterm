# Generated by Django 5.1.4 on 2024-12-30 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ResaleFlat",
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
                ("month", models.CharField(max_length=20)),
                ("town", models.CharField(max_length=100)),
                ("flat_type", models.CharField(max_length=50)),
                ("block", models.CharField(max_length=10)),
                ("street_name", models.CharField(max_length=255)),
                ("storey_range", models.CharField(max_length=50)),
                ("floor_area_sqm", models.FloatField()),
                ("flat_model", models.CharField(max_length=100)),
                ("lease_commence_date", models.IntegerField()),
                ("remaining_lease", models.IntegerField()),
                ("resale_price", models.FloatField()),
            ],
        ),
    ]
