import requests

url = "https://ru.yougile.com/api-v2/auth/keys"

data = {
    "login": "ТВОЙ_EMAIL",
    "password": "ТВОЙ_ПАРОЛЬ",
    "companyId": "ID_КОМПАНИИ"
}

response = requests.post(
    url,
    json=data,
    headers={
        "Content-Type": "application/json"
    }
)

print(response.status_code)
print(response.json())
