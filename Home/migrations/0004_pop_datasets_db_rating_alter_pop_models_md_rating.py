# Generated by Django 4.2.1 on 2024-01-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0003_feedbacks"),
    ]

    operations = [
        migrations.AddField(
            model_name="pop_datasets",
            name="db_rating",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pop_models",
            name="md_rating",
            field=models.FloatField(blank=True, null=True),
        ),
    ]