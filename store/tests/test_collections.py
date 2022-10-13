import pytest
from rest_framework import status


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post("/store/collections/", collection)
    return do_create_collection


@pytest.fixture
def delete_collection(api_client):
    def do_delete_collection(collection):
        return api_client.delete("/store/collections/", collection)
    return do_delete_collection


#Arrange, Act, Assert
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        response = create_collection({"title": "a"})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_user_is_not_admin_returns_403(self, api_client, create_collection, authenticate):
        authenticate()
        response = create_collection({"title": "a"})

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_data_is_invalid_returns_400(self, api_client, create_collection, authenticate):
        authenticate(True)
        response = create_collection({"title": ""})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] is not None


    def test_if_data_is_valid_returns_201(self, api_client, create_collection, authenticate):
        authenticate(True)
        response = create_collection({"title": "a"})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0


class TestDeleteCollection:
    def test_if_user_is_anonymous_returns_401(self, delete_collection):
        response = delete_collection({"title": "a"})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_user_is_not_admin_returns_403(self, delete_collection, authenticate):
        authenticate()
        response = delete_collection({"title": "a"})

        assert response.status_code == status.HTTP_403_FORBIDDEN
 

