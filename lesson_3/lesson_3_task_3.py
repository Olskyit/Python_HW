from address import Address
from mailing import Mailing

to_address = Address(
    "191181",
    "Санкт-Петербург",
    "Невский проспект",
    "10",
    "15"
)

from_address = Address(
    "101000",
    "Москва",
    "Тверская",
    "25",
    "8"
)

mailing = Mailing(
    to_address,
    from_address,
    500,
    "TR123456789RU"
)

print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, "
    f"{mailing.from_address.street}, "
    f"{mailing.from_address.house} - "
    f"{mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, "
    f"{mailing.to_address.city}, "
    f"{mailing.to_address.street}, "
    f"{mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
