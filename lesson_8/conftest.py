import uuid

import pytest

from project_api import ProjectApi


@pytest.fixture
def new_project():

    title = f"Test project {uuid.uuid4()}"

    response = ProjectApi.create_project(title)

    assert response.status_code == 201

    project_id = response.json()["id"]

    yield project_id


    ProjectApi.delete_project(project_id)
