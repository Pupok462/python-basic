# Generated by Django 4.1 on 2022-08-12 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Devices",
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
                ("company", models.CharField(max_length=64)),
                ("model", models.CharField(max_length=64)),
                ("price", models.FloatField(null=True)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="DevicesType",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name="Laptop",
        ),
        migrations.DeleteModel(
            name="Phone",
        ),
        migrations.DeleteModel(
            name="Tablet",
        ),
        migrations.AddField(
            model_name="devices",
            name="type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="devices.devicestype",
            ),
        ),
    ]
