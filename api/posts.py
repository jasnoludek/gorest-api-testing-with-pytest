import requests
from config import ACCESS_TOKEN, ENDPOINT, USERS_API


def create_new_post(user_id, new_post_payload):
    """
    Create a new post using the GoRest API and the user's ID.
    """
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    return requests.post(ENDPOINT + USERS_API + f'{user_id}/posts', json=new_post_payload, headers=headers)


def get_post(new_user_id):
    """
    Retrieve a post using the GoRest API and the user's ID.
    """
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    return requests.get(ENDPOINT + USERS_API + f'{new_user_id}/posts', headers=headers)
