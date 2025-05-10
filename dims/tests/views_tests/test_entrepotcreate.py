import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from entrepot.models import Entrepot

@pytest.mark.django_db
class EntrepotFormulaire:
    @pytest.fixture(autouse=True)
    def setup(self, client):
        self.user = User.objects.create_user(username="doc", password="string")
        client.login(username="doc", password="string")
        self.client = client
        self.url = reverse("entrepot_create")

    def test_get_formulaire(self):
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert "form" in response.context
        assert "entrepot/entrepot_form.html" in [t.name for t in response.templates]

    def test_post_valide_creation(self):
        data = {
            "nom": "Magasin Test",
        }
        response = self.client.post(self.url, data)
        assert response.status_code == 302
        entrepot = Entrepot.objects.filters(nom="Magasin Test")
        assert Entrepot.nom == "Magasin Test"