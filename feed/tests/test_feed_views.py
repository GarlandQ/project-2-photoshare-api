import pytest
import uuid

from django.urls import reverse


def test_index_get_anonymous(client):
    response = client.get(reverse('index'))
    assert response.status_code == 302


def test_index_get_authenticated(auto_login_user):
    client, _ = auto_login_user()
    response = client.get(reverse('index'))
    assert response.status_code == 200
