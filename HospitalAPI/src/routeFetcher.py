import os
from dotenv import load_dotenv
import googlemaps
import math

def calculate_distance_duration(origin, destination):
    load_dotenv()
    api_key = os.getenv("API_KEY")

    gmaps = googlemaps.Client(key=api_key)

    try:
        matrix = gmaps.distance_matrix(origin, destination)

        # Check if the response has the expected structure
        if 'rows' in matrix and matrix['rows'] and 'elements' in matrix['rows'][0] and matrix['rows'][0]['elements']:
            distance = matrix['rows'][0]['elements'][0].get('distance', {}).get('text', 'N/A')
            duration = matrix['rows'][0]['elements'][0].get('duration', {}).get('text', 'N/A')

            if distance == 'N/A' or duration == 'N/A':
                return math.inf, math.inf
        else:
            raise ValueError("Unexpected response structure from Google Maps API.")

    except googlemaps.exceptions.ApiError as e:
        raise ValueError(f"Error from Google Maps API: {str(e)}")

    return distance, duration
