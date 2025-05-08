# OpenWMS
# en: Project for Django Python Course
# fr: Projet pour un cours Django


# V 0.0 du 08/05/2025
    Début du projet


# ROADMAP V1.0

**Gestion des stocks**

1. Gestion des utilisateurs et rôles
    Inscription, authentification, réinitialisation de mot de passe.
2. Catalogue produits
   CRUD complet, import/export CSV.
3. Multi-entreprises
   Possibilité de gérer les stocks de plusieurs entreprises, chaque utilisateur étant limité à son périmètre (on peut affecter un utilisateur à une ou plusieurs entreprises).
4. Mouvements de stock
   Entrées, sorties, historisation avec horodatage.
5. Alertes seuil critique
   Notification dans l'application lorsque la quantité passe sous le seuil défini et possibilité pour chaque produit de définir le seuil d'alerte.
6. Tableau de bord & statistiques
   Graphiques simples (quantités par catégorie, évolution mensuelle) rendus avec Chart.js.
7. Administration personnalisée
   Interface admin (affichage, filtres, recherche) permettant la gestion des utilisateurs, produits, stocks, etc.
