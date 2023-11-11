from utils.user_utils import create_new_user_payload
from utils.post_utils import create_new_post_payload
from api.user import create_new_user
from api.posts import create_new_post, get_post


def test_can_create_post():
    """
    Test the ability to create a new post through the API.
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

    # Parse the JSON response to extract data from the new post
    create_new_post_response_data = create_new_post_response.json()

    # Validate the new post creation response data
    assert create_new_post_response_data['user_id'] == new_user_id
    assert create_new_post_response_data['title'] == new_post_payload['title']
    assert create_new_post_response_data['body'] == new_post_payload['body']


def test_can_get_post():
    """
    Test the ability to retrieve a post through the API.
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

    # Parse the JSON response to extract data from the new post
    create_new_post_response_data = create_new_post_response.json()

    # Extract new post ID from the response data
    new_post_id = create_new_post_response_data['id']

    # Make request to retrieve the new post data
    get_new_post_response = get_post(new_user_id)
    assert get_new_post_response.status_code == 200

    # Extract data from the response
    get_new_post_response_data = get_new_post_response.json()

    # Search for the post using matching post ID
    retrieved_post = next(post for post in get_new_post_response_data if post['id'] == new_post_id)

    # Validate data of retrieved created post
    assert retrieved_post['id'] == new_post_id
    assert retrieved_post['user_id'] == new_user_id
    assert retrieved_post['title'] == new_post_payload['title']
    assert retrieved_post['body'] == new_post_payload['body']
