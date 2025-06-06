# Generated by Django 5.2.1 on 2025-05-10 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255, verbose_name='Libelle')),
                ('rue', models.CharField(max_length=255, verbose_name='Rue et numéro')),
                ('complement', models.CharField(blank=True, max_length=255, verbose_name="Complément d'adresse")),
                ('ville', models.CharField(max_length=100, verbose_name='Ville')),
                ('etat', models.CharField(blank=True, max_length=100, verbose_name='État / Région')),
                ('cp', models.CharField(max_length=20, verbose_name='Code postal')),
                ('pays', models.CharField(max_length=100, verbose_name='Pays')),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adresses',
                'ordering': ['pays', 'ville', 'rue'],
            },
        ),
        migrations.CreateModel(
            name='TypeMouvement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Type de Mouvement',
                'verbose_name_plural': 'Types de Mouvement',
                'ordering': ['libelle'],
            },
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('adresse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entreprise_adresse', to='entrepot.adresse')),
            ],
            options={
                'verbose_name': 'Entreprise',
                'verbose_name_plural': 'Entreprises',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Entrepot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrepot_adresse', to='entrepot.adresse')),
                ('entreprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entreprises', to='entrepot.entreprise')),
            ],
            options={
                'verbose_name': 'Entrepot',
                'verbose_name_plural': 'Entrepot',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Mouvement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('quantite', models.IntegerField()),
                ('entrepot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrepot', to='entrepot.entrepot')),
                ('type_mouvement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='entrepot.typemouvement')),
            ],
            options={
                'verbose_name': 'Mouvement',
                'verbose_name_plural': 'Mouvements',
                'ordering': ['date'],
            },
        ),
    ]
