from utils.common_utils import generate_random_string, generate_random_email


def create_new_comment_payload(post=None):
    """
    Generate a random comment with a unique body for testing comment creation.
    """
    name = generate_random_string()
    email = generate_random_email()
    body = generate_random_string()

    payload = {
        "post": post if post is not None else '',
        "name": name,
        "email": email,
        "body": body
    }

    return payload

