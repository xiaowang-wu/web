# Generated by Django 5.0.3 on 2024-03-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myweb", "0002_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="Static",
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
                ("salary", models.CharField(max_length=32, verbose_name="薪资")),
                ("months", models.CharField(max_length=32, verbose_name="月份")),
                ("work", models.CharField(max_length=32, verbose_name="工作量")),
            ],
        ),
    ]
