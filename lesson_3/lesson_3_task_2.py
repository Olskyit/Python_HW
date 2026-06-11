from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79991111111"),
    Smartphone("Samsung", "Galaxy S24", "+79992222222"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79993333333"),
    Smartphone("Huawei", "P60", "+79994444444"),
    Smartphone("Honor", "Magic6", "+79995555555")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
