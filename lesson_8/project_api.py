import requests

from config import BASE_URL, HEADERS


class ProjectApi:

    @staticmethod
    def create_project(title):
        body = {
            "title": title
        }

        return requests.post(
            f"{BASE_URL}/projects",
            json=body,
            headers=HEADERS
        )

    @staticmethod
    def get_project(project_id):
        return requests.get(
            f"{BASE_URL}/projects/{project_id}",
            headers=HEADERS
        )

    @staticmethod
    def update_project(project_id, title):
        body = {
            "title": title
        }

        return requests.put(
            f"{BASE_URL}/projects/{project_id}",
            json=body,
            headers=HEADERS
        )

    @staticmethod
    def delete_project(project_id):
        body = {
            "deleted": True
        }

        return requests.put(
            f"{BASE_URL}/projects/{project_id}",
            json=body,
            headers=HEADERS
        )
