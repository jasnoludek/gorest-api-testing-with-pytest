import uuid
import random


def generate_random_string():
    """
    Generate a random string for testing purposes.
    """
    random_string = f'test_string_{uuid.uuid4().hex}'
    return random_string


def generate_random_email():
    """
    Generate a random email address for testing purposes.
    """
    unique_id = uuid.uuid4().hex[:12]
    domain = 'example.com'
    return f'random_{unique_id}@{domain}'


days_in_month = {
    1: 31,  # January
    2: 28,  # February (assuming non-leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31,  # December
}


def generate_random_date():
    """
    Generate a random date for testing purposes.
    """
    year = random.randint(2023, 2024)
    month = random.randint(1, 12)
    max_days = days_in_month[month]
    day = random.randint(1, max_days)
    random_date = f'{year:04d}-{month:02d}-{day:02d}'
    return random_date
