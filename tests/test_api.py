"""
API tests demonstrating requests + pytest fundamentals.

Note: saucedemo.com has no public API, so these tests run against
reqres.in (a public fake-API testing service) purely to demonstrate
API testing skills, separate from the UI test suite above.
"""
import requests


def test_get_single_user_returns_200():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    data = response.json()
    assert data["data"]["id"] == 2, f"Expected id 2 but got {data['data']['id']}"
    assert data["data"]["email"] == "janet.weaver@reqres.in", f"Unexpected email: {data['data']['email']}"


def test_create_user_returns_201():
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post("https://reqres.in/api/users", json=payload)

    assert response.status_code == 201, f"Expected 201 but got {response.status_code}"

    data = response.json()
    assert data["name"] == "morpheus", f"Expected name 'morpheus' but got '{data['name']}'"
    assert data["job"] == "leader", f"Expected job 'leader' but got '{data['job']}'"


def test_get_nonexistent_user_returns_404():
    response = requests.get("https://reqres.in/api/users/9999")
    assert response.status_code == 404, f"Expected 404 but got {response.status_code}"


def test_get_users_list_returns_multiple_users():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    data = response.json()
    assert len(data["data"]) > 0, f"Expected multiple users but got {len(data['data'])}"
