import requests
import uuid

from config import ENDPOINT
from utils.user_utils import create_new_user_payload, generate_random_email
from api.user import create_new_user, get_user, update_user, delete_user


def test_can_call_endpoint():
    """
    Tests if the API endpoint is accessible.
    """
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_can_create_user():
    """
    Tests the creation of a user and validation of user data.
    """

    # Create a new user
    new_user_payload = create_new_user_payload()
    create_new_user_response = create_new_user(new_user_payload)
    assert create_new_user_response.status_code == 201

    # Extract the new user's ID
    create_new_user_response_data = create_new_user_response.json()
    new_user_id = create_new_user_response_data['id']

    # Retrieve the new user with user ID
    get_new_user_response = get_user(new_user_id)
    assert get_new_user_response.status_code == 200

    # Parse the JSON response to extract new user data
    get_new_user_response_data = get_new_user_response.json()

    # Validate new user data
    assert get_new_user_response_data['name'] == new_user_payload['name']
    assert get_new_user_response_data['gender'] == new_user_payload['gender']
    assert get_new_user_response_data['email'] == new_user_payload['email']
    assert get_new_user_response_data['status'] == new_user_payload['status']


def test_can_update_user():
    """
    Tests the ability to update user data.
    """

    # Create a new user
    new_user_payload = create_new_user_payload()
    create_new_user_response = create_new_user(new_user_payload)
    assert create_new_user_response.status_code == 201

    # Extract the new user's ID
    create_new_user_response_data = create_new_user_response.json()
    new_user_id = create_new_user_response_data['id']

    # New payload to update user data
    update_user_payload = {
        'name': f'test_user_{uuid.uuid4().hex}',
        'gender': 'male',
        'email': generate_random_email(),
        'status': 'active'
    }

    # Update user data with user ID and new payload
    update_user_response = update_user(new_user_id, update_user_payload)
    assert update_user_response.status_code == 200

    # Parse the JSON response to extract updated user data
    update_user_response_data = update_user_response.json()

    # Validate updated user data
    assert update_user_response_data['name'] == update_user_payload['name']
    assert update_user_response_data['gender'] == update_user_payload['gender']
    assert update_user_response_data['email'] == update_user_payload['email']
    assert update_user_response_data['status'] == update_user_payload['status']


def test_can_delete_user():
    """
    Tests the ability to delete a user
    """

    # Create a new user
    new_user_payload = create_new_user_payload()
    create_new_user_response = create_new_user(new_user_payload)
    assert create_new_user_response.status_code == 201

    # Extract the new user's ID
    create_new_user_response_data = create_new_user_response.json()
    new_user_id = create_new_user_response_data['id']

    # Delete the new user with user ID
    delete_user_response = delete_user(new_user_id)
    assert delete_user_response.status_code == 204

    # Validate user data not found when attempting to retrieve with user ID
    assert not delete_user_response.text
