import requests

BASE_URL = 'http://127.0.0.1:5000/'


def create_user(name, email):
    response = requests.post(BASE_URL + 'users', json={"name": name, "email": email})
    return response.json()


def get_users():
    response = requests.get(BASE_URL + 'users')
    return response.json()

def update_user(user_id, name=None, email=None):
    data = {}
    if name:
        data['name'] = name
    if email:
        data['email'] = email
    response = requests.put(BASE_URL + f'users/{user_id}', json=data)
    return response.json()

def delete_user(user_id):
    response = requests.delete(BASE_URL + f'users/{user_id}')
    return response.json()

# for example
if __name__ == '__main__':
    user = create_user('Takhmina', 'tt@example.com')
    print("Created user:", user)

    users = get_users()
    print("All users:", users)

    if users:
        user_id = users[0]['id']
        updated = update_user(user_id, name='John Smith')
        print("Updated user:", updated)

        deleted = delete_user(user_id)
        print("Deleted user:", deleted)
