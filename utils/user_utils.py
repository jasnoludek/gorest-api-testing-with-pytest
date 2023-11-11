from utils.common_utils import generate_random_string, generate_random_email


def create_new_user_payload():
    """
    Generate a random new user payload with a unique name, gender, email, and status for testing user creation.
    """
    name = generate_random_string()
    gender = 'female'
    email = generate_random_email()
    status = 'inactive'

    return {
        'name': name,
        'gender': gender,
        'email': email,
        'status': status
    }
