# Generated by Django 5.0.2 on 2024-02-27 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("currencies", "0002_alter_currency_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="CurrencyAverage",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("date", models.DateField(unique_for_month=True)),
                ("currency", models.CharField(max_length=10)),
                (
                    "buying",
                    models.DecimalField(decimal_places=15, default=0, max_digits=40),
                ),
                (
                    "selling",
                    models.DecimalField(decimal_places=15, default=0, max_digits=40),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
