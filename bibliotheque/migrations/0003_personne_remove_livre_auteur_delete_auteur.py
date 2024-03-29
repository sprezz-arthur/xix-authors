# Generated by Django 4.1.4 on 2023-01-15 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bibliotheque", "0002_remove_livre_auteur_livre_auteur"),
    ]

    operations = [
        migrations.CreateModel(
            name="Personne",
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
                ("nom", models.CharField(max_length=200)),
                ("prenom", models.CharField(max_length=100)),
                ("date_naissance", models.DateField(null=True)),
                ("date_mort", models.DateField(null=True)),
                ("lieu_naissance", models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name="livre",
            name="auteur",
        ),
        migrations.DeleteModel(
            name="Auteur",
        ),
    ]
