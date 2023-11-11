from utils.user_utils import create_new_user_payload
from utils.todos_utils import create_new_todo_payload
from api.user import create_new_user
from api.todos import create_new_todo, retrieve_user_todo_list


def test_can_create_new_todo():
    """
    Test the ability to create a new to-do through the API.
    """

    # Create a new user
    new_user_payload = create_new_user_payload()
    create_new_user_response = create_new_user(new_user_payload)
    assert create_new_user_response.status_code == 201

    # Extract the new user's ID
    create_new_user_response_data = create_new_user_response.json()
    new_user_id = create_new_user_response_data['id']

    # Create a new to-do using the new user's ID
    new_todo_payload = create_new_todo_payload()
    create_new_todo_response = create_new_todo(new_user_id, new_todo_payload)
    assert create_new_todo_response.status_code == 201

    # Parse the JSON response to extract data from the new to-do
    create_new_todo_response_data = create_new_todo_response.json()

    # Validate the new to-do creation response data
    assert create_new_todo_response_data['user_id'] == new_user_id
    assert create_new_todo_response_data['title'] == new_todo_payload['title']
    assert create_new_todo_response_data['due_on'].split('T')[0] == new_todo_payload['due_on']
    assert create_new_todo_response_data['status'] == new_todo_payload['status']


def test_can_retrieve_user_todo_list():
    """
    Test the ability to retrieve a list of to-do's with user ID.
    """

    # Create a new user
    new_user_payload = create_new_user_payload()
    create_new_user_response = create_new_user(new_user_payload)
    assert create_new_user_response.status_code == 201

    # Extract the new user's ID
    create_new_user_response_data = create_new_user_response.json()
    new_user_id = create_new_user_response_data['id']

    # Create a new to-do using the new user's ID
    new_todo_payload = create_new_todo_payload()
    create_new_todo_response = create_new_todo(new_user_id, new_todo_payload)
    assert create_new_todo_response.status_code == 201

    # Retrieve the new to-do list
    retrieve_user_todo_list_response = retrieve_user_todo_list(new_user_id)
    assert retrieve_user_todo_list_response.status_code == 200

    # Get the first to-do from the list
    retrieve_new_todo_data = retrieve_user_todo_list_response.json()[0]

    # Validate to-do retrieval response data
    assert retrieve_new_todo_data['user_id'] == new_user_id
    assert retrieve_new_todo_data['title'] == new_todo_payload['title']
    assert retrieve_new_todo_data['due_on'].split('T')[0] == new_todo_payload['due_on']
    assert retrieve_new_todo_data['status'] == new_todo_payload['status']
