# Generated by Django 4.1.4 on 2023-02-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bibliotheque", "0005_faitmarquant_rename_faithistorique_faitsocial_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personne",
            name="amis",
            field=models.ManyToManyField(blank=True, to="bibliotheque.personne"),
        ),
    ]