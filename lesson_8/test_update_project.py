import uuid

from project_api import ProjectApi


def test_update_project_positive(new_project):
    new_title = f"Updated {uuid.uuid4()}"

    response = ProjectApi.update_project(
        new_project,
        new_title
    )

    assert response.status_code == 200

    project = ProjectApi.get_project(new_project)

    assert project.json()["title"] == new_title


def test_update_project_wrong_id():
    response = ProjectApi.update_project(
        "00000000-0000-0000-0000-000000000000",
        "Test"
    )

    assert response.status_code == 404

    assert "error" in response.json()
