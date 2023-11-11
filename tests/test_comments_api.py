from utils.user_utils import create_new_user_payload
from utils.post_utils import create_new_post_payload
from utils.comment_utils import create_new_comment_payload
from api.user import create_new_user
from api.posts import create_new_post
from api.comments import create_new_comment, get_comment


def test_can_create_comment():
    """
    Test the ability to create a new comment through the API.
    """

    # Create a new user
    new_user_payload = create_new_user_payload()
    create_new_user_response = create_new_user(new_user_payload)
    assert create_new_user_response.status_code == 201

    # Extract the new user's ID
    create_new_user_response_data = create_new_user_response.json()
    new_user_id = create_new_user_response_data['id']

    # Create a new post using the new user's ID
    new_post_payload = create_new_post_payload()
    create_new_post_response = create_new_post(new_user_id, new_post_payload)
    assert create_new_post_response.status_code == 201

    # Extract the new post ID
    create_new_post_response_data = create_new_post_response.json()
    new_post_id = create_new_post_response_data['id']

    # Create a new comment using the new post ID
    new_comment_payload = create_new_comment_payload(post=new_post_id)
    create_new_comment_response = create_new_comment(new_post_id, new_comment_payload)
    assert create_new_comment_response.status_code == 201

    # Validate new comment creation response data
    create_new_comment_response_data = create_new_comment_response.json()
    assert create_new_comment_response_data['post_id'] == new_comment_payload['post']
    assert create_new_comment_response_data['name'] == new_comment_payload['name']
    assert create_new_comment_response_data['email'] == new_comment_payload['email']
    assert create_new_comment_response_data['body'] == new_comment_payload['body']

def test_can_retrieve_comment():
    """
    Test the ability to retrieve comments for a post using post ID.
    """

    # Create a new user
    new_user_payload = create_new_user_payload()
    create_new_user_response = create_new_user(new_user_payload)
    assert create_new_user_response.status_code == 201

    # Extract the new user's ID
    create_new_user_response_data = create_new_user_response.json()
    new_user_id = create_new_user_response_data['id']

    # Create a new post using the new user's ID
    new_post_payload = create_new_post_payload()
    create_new_post_response = create_new_post(new_user_id, new_post_payload)
    assert create_new_post_response.status_code == 201

    # Extract the new post ID
    create_new_post_response_data = create_new_post_response.json()
    new_post_id = create_new_post_response_data['id']

    # Create a new comment using the new post ID
    new_comment_payload = create_new_comment_payload(post=new_post_id)
    create_new_comment_response = create_new_comment(new_post_id, new_comment_payload)
    assert create_new_comment_response.status_code == 201

    # Retrieve the new comment
    retrieve_comment_response = get_comment(new_post_id)
    assert retrieve_comment_response.status_code == 200

    # Get the first comment from the list
    retrieve_comment_response_data = retrieve_comment_response.json()[0]

    # Validate comment response data
    assert retrieve_comment_response_data['post_id'] == new_comment_payload['post']
    assert retrieve_comment_response_data['name'] == new_comment_payload['name']
    assert retrieve_comment_response_data['email'] == new_comment_payload['email']
    assert retrieve_comment_response_data['body'] == new_comment_payload['body']


