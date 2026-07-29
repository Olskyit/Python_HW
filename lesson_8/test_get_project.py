import uuid

from project_api import ProjectApi


def test_get_project_positive(new_project):

    response = ProjectApi.get_project(new_project)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == new_project


def test_get_project_wrong_id():

    fake_id = str(uuid.uuid4())

    response = ProjectApi.get_project(fake_id)

    assert response.status_code == 404

    assert "error" in response.json()
