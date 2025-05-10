import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_login(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    templates_utilises = [t.name for t in response.templates]
    assert 'entrepot/login.html' in templates_utilises