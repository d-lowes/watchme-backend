import requests

# Make a request to the API to grab a show based on its show ID

API_SHOW_URL = "https://api.example.com/shows"

def fetch_show_details(show_id):
    """send a show ID to the API and return json"""

    try:
        response = requests.get(f'{API_SHOW_URL}/{show_id}')
        response.raise_for_status()

        show_details = response.json()
    except requests.exceptions.RequestException as error:
        print(f'An error occured: {error}')
        return None
