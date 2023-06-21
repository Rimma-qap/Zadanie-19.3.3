import json

import requests

BASE_URL = "https://petstore.swagger.io/v2/pet/"


def get_pet(pet_id):
    """Получение информации о питомце"""

    resp = requests.get(
        f"{BASE_URL}{pet_id}",
        headers={"accept": "application/json"},
    )
    print("GET-запрос, код статуса:", resp.status_code)
    print("Response:", resp.json())


def add_pet(new_pet):
    """Добавление нового питомца"""

    resp = requests.post(
        BASE_URL,
        data=json.dumps(new_pet),
        headers={
            "accept": "application/json",
            "Content-Type": "application/json",
        },
    )
    print("POST-запрос, код статуса:", resp.status_code)
    print("Response:", resp.json())


def update_pet(pet):
    """Обновление информации о питомце"""

    resp = requests.put(
        BASE_URL,
        data=json.dumps(pet),
        headers={
            "accept": "application/json",
            "Content-Type": "application/json",
        },
    )
    print("PUT-запрос, код статуса:", resp.status_code)
    print("Response:", resp.json())


def delete_pet(pet_id):
    """Удаление питомца"""

    resp = requests.delete(
        f"{BASE_URL}{pet_id}",
        headers={"accept": "application/json"},
    )
    print("DELETE-запрос, код статуса:", resp.status_code)
    print("Response:", resp.json())


def main():
    pet_id = 9223372036854775807
    get_pet(pet_id)

    new_pet = {
        "id": pet_id,
        "category": {"id": 100, "name": "dog"},
        "name": "Brown",
        "photoUrls": ["images/dog.jpeg"],
        "tags": [{"id": 200, "name": "gav"}],
        "status": "available",
    }
    add_pet(new_pet)

    new_pet["name"] = "Baks"
    update_pet(new_pet)

    delete_pet(pet_id)


if __name__ == "__main__":
    main()
