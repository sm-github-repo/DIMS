from django.contrib import admin
from entrepot.models import Entreprise, Entrepot, Adresse,Mouvement, TypeMouvement
# Register your models here.


admin.site.register(Entreprise)
admin.site.register(Entrepot)
admin.site.register(Adresse)
admin.site.register(Mouvement)
admin.site.register(TypeMouvement)