# Generated by Django 4.1.1 on 2022-09-19 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("tittle", models.CharField(max_length=32)),
                ("content", models.CharField(max_length=2048)),
            ],
        ),
    ]
