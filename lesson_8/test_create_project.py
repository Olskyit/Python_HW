import uuid

from project_api import ProjectApi


def test_create_project_positive():

    title = f"Project {uuid.uuid4()}"

    response = ProjectApi.create_project(title)

    assert response.status_code == 201

    body = response.json()

    assert "id" in body
    assert body["title"] == title


def test_create_project_without_title():

    response = ProjectApi.create_project(None)

    assert response.status_code == 400

    body = response.json()

    assert "error" in body
