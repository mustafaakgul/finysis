# Generated by Django 5.0.2 on 2024-02-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financials", "0003_alter_mizan_credit_alter_mizan_credit_balance_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mizan",
            name="debit",
            field=models.CharField(default="0", max_length=50),
        ),
    ]