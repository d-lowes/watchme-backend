import requests

# Make a request to the API to grab a show based on its show ID

API_SHOW_URL = "https://api.example.com/shows"


def fetch_show_details(show_title):
    """Send a show ID to the API and return json information about the show.

    querystring = {
        "title": show_id,
        "country":"us",
        "show_type":"movie",
        "output_language":"en"
        }

    headers = {
            "X-RapidAPI-Key": "API KEY",
            "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
    }

    response = requests.get(API_SHOW_URL, headers=headers, params=querystring)
    """

    try:
        response = requests.get(f'{API_SHOW_URL}/{show_title}')
        response.raise_for_status()

        show_details = response.json()
        return show_details

    except requests.exceptions.RequestException as error:
        print(f'An error occured: {error}')
        return None
