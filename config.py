from configparser import ConfigParser

config = ConfigParser()
config.read('auth.ini')

ACCESS_TOKEN = config.get('API', 'ACCESS_TOKEN')

ENDPOINT = 'https://gorest.co.in'

USERS_API = '/public/v2/users/'

POSTS_API = f'/public/v2/posts/'

COMMENTS_API = f'/public/v2/posts/'

TODOS_API = f'/public/v2/users/'
