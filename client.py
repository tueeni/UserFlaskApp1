import requests

BASE_URL = 'http://127.0.0.1:5000/'


def create_user(name, email):
    response = requests.post(BASE_URL + 'users', json={"name": name, "email": email})
    return response.json()


def get_users():
    response = requests.get(BASE_URL + 'users')
    return response.json()


# for example
if __name__ == '__main__':
    # Создаем пользователя
    user = create_user('John Doe', 'john@example.com')
    print("Created user:", user)

    # Получаем всех пользователей
    users = get_users()
    print("All users:", users)
