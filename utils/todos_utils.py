from utils.common_utils import generate_random_string, generate_random_date


def create_new_todo_payload():
    """
    Generate a random to-do with a unique body for testing comment creation.
    """
    title = generate_random_string()
    random_date = generate_random_date()
    status = 'completed'

    payload = {
        "title": title,
        "due_on": random_date,
        "status": status
    }

    return payload
