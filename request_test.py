import requests

from configurations import SERVICE_URL

from src.baseclasses.base_response_second import Response_two
from src.pydantic_schemas.post import Post

def tests_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response_two(r)
    response.assert_status_code(200).validate(Post)

    ##[{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]


