import os

import googlemaps
from dotenv import load_dotenv

def calculate_distance_duration(origin, destination):

    load_dotenv()
    api_key = os.getenv("API_KEY")
    gmaps = googlemaps.Client(key=api_key)

    matrix = gmaps.distance_matrix(origin, destination)

    distance = matrix['rows'][0]['elements'][0]['distance']['text']
    duration = matrix['rows'][0]['elements'][0]['duration']['text']

    return distance, duration