# Generated by Django 4.2.1 on 2024-01-02 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0002_pop_datasets_delete_pop_databases"),
    ]

    operations = [
        migrations.CreateModel(
            name="feedbacks",
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
                ("feed_name", models.CharField(max_length=20)),
                ("feed_message", models.CharField(max_length=100)),
                ("feed_rating", models.FloatField(blank=True, null=True)),
                ("feed_logo", models.ImageField(upload_to="images/logos")),
            ],
        ),
    ]
