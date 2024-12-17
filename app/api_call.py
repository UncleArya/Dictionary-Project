# Modules
import requests

# Constants
BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def call_api(query_keyword):

    request = requests.get(
        f"{BASE_URL}{query_keyword}"
    )
    return request.json()
