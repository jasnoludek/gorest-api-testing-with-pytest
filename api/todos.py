import requests
from config import ACCESS_TOKEN, ENDPOINT, TODOS_API


def create_new_todo(new_user_id, create_new_todo_payload):
    """
    Create a new to-do using the GoRest API.
    """
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    return requests.post(ENDPOINT + TODOS_API + f'{new_user_id}/todos', json=create_new_todo_payload, headers=headers)


def retrieve_user_todo_list(new_user_id):
    """
    Retrieve full list of to-do's for a user with the user's ID.
    """
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    return requests.get(ENDPOINT + TODOS_API + f'{new_user_id}/todos', headers=headers)