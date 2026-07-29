import uuid

from project_api import ProjectApi


def test_create_project_positive():
    title = f"Project {uuid.uuid4()}"

    response = ProjectApi.create_project(title)

    assert response.status_code == 201

    body = response.json()

    assert "id" in body

    project_id = body["id"]

    project = ProjectApi.get_project(project_id)

    assert project.json()["title"] == title

    ProjectApi.delete_project(project_id)


def test_create_project_without_title():
    response = ProjectApi.create_project("")

    assert response.status_code in [400, 422]

    assert "error" in response.json()
