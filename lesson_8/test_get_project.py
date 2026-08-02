from project_api import ProjectApi


def test_get_project_positive(new_project):
    response = ProjectApi.get_project(new_project)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == new_project

    assert "title" in body


def test_get_project_wrong_id():
    response = ProjectApi.get_project(
        "00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code == 404

    assert "error" in response.json()
