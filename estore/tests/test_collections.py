from rest_framework import status
from rest_framework.test import APIClient
import pytest


#Arrange, Act, Assert
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self):
        client = APIClient()
        response = client.post("/store/collections/", {"title": "a"})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

class TestDeleteCollection:
    def test_if_user_is_anonymous_returns_401(self):
        client = APIClient()
        response = client.delete("/store/collections/")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED