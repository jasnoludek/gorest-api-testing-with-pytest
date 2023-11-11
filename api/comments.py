import requests
from config import ACCESS_TOKEN, ENDPOINT, COMMENTS_API


def create_new_comment(new_post_id, new_comment_payload):
    """
    Create a new comment using the GoRest API and the user's ID.
    """
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    return requests.post(ENDPOINT + COMMENTS_API + f'{new_post_id}/comments', json=new_comment_payload, headers=headers)


def get_comment(new_post_id):
    """
    Retrieve a comment using the GoRest API and the user's ID.
    """
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    return requests.get(ENDPOINT + COMMENTS_API + f'{new_post_id}/comments', headers=headers)