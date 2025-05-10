from django.db import models
from django.utils.text import slugify


class Adresse(models.Model):
    libelle = models.CharField("Libelle", max_length=255)
    rue = models.CharField("Rue et numéro", max_length=255)
    complement = models.CharField("Complément d'adresse", max_length=255, blank=True)
    ville = models.CharField("Ville", max_length=100)
    etat = models.CharField("État / Région", max_length=100, blank=True)
    cp = models.CharField("Code postal", max_length=20)
    pays = models.CharField("Pays", max_length=100)

    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"
        ordering = ['pays', 'ville', 'rue']

    def __str__(self):
        return self.libelle


class Entreprise(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    adresse = models.ForeignKey(
        Adresse,
        on_delete=models.CASCADE,
        related_name='entreprise_adresse',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Entreprise"
        verbose_name_plural = "Entreprises"
        ordering = ['nom']

    def __str__(self):
        return self.nom


class Entrepot(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    entreprise = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        related_name='entreprises'
    )
    adresse = models.ForeignKey(
        Adresse,
        on_delete=models.CASCADE,
        related_name='entrepot_adresse'
    )

    class Meta:
        verbose_name = "Entrepot"
        verbose_name_plural = "Entrepot"
        ordering = ['nom']

    def __str__(self):
        return self.nom


class TypeMouvement(models.Model):
    libelle = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name = "Type de Mouvement"
        verbose_name_plural = "Types de Mouvement"
        ordering = ['libelle']

    def __str__(self):
        return self.libelle


class Mouvement(models.Model):
    date = models.DateTimeField()
    quantite = models.IntegerField()
    type_mouvement = models.ForeignKey(
        TypeMouvement,
        on_delete=models.CASCADE,
        related_name='type'
    )
    entrepot = models.ForeignKey(
        Entrepot,
        on_delete=models.CASCADE,
        related_name='entrepot',
    )


    class Meta:
        verbose_name = "Mouvement"
        verbose_name_plural = "Mouvements"
        ordering = ['date']

    def __str__(self):
        return f"{self.date} {self.type_mouvement.libelle}"
