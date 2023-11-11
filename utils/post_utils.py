from utils.common_utils import generate_random_string


def create_new_post_payload():
    """
    Generate a random post with a unique title and body for testing post creation.
    """
    title = generate_random_string()
    body = generate_random_string()

    return {
        'title': title,
        'body': body
    }
