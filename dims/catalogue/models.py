from django.db import models
from django.db import models
from django.utils.text import slugify

class Categorie(models.Model):
    """
    Une catégorie pour organiser les produits.
    """
    libelle = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ['libelle']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.libelle)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.libelle


class Article(models.Model):
    """
    Un article simple lié à une catégorie.
    """
    ref = models.CharField(max_length=50,unique=True)
    EAN = models.CharField(max_length=13,unique=True)
    libelle = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, editable=False)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['libelle']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.libelle)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.libelle} ({self.categorie.name})"
