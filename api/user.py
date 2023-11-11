import requests
from config import ACCESS_TOKEN, ENDPOINT, USERS_API


def create_new_user(new_user_payload):
    """
    Create a new user using the GoRest API.
    """
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    return requests.post(ENDPOINT + USERS_API, json=new_user_payload, headers=headers)


def get_user(new_user_id):
    """
    Retrieve user data from the GoRest API using the user's ID.
    """
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    return requests.get(ENDPOINT + USERS_API + f'{new_user_id}', headers=headers)


def update_user(new_user_id, update_user_payload):
    """
    Update user data using the GoRest API with the specified user ID and payload.
    """
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    return requests.put(ENDPOINT + USERS_API + f'{new_user_id}', json=update_user_payload, headers=headers)


def delete_user(new_user_id):
    """
    Delete a user using the GoRest API with the specified user ID.
    """
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    return requests.delete(ENDPOINT + USERS_API + f'{new_user_id}', headers=headers)