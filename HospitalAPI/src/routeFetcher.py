import os
from dotenv import load_dotenv
import googlemaps
import math

def calculate_distance_duration(origin, hospitals):
    load_dotenv()
    api_key = os.getenv("API_KEY")

    gmaps = googlemaps.Client(key=api_key)

    try:
        batch_size = 25
        for i in range(0, len(hospitals), batch_size):
            batch_hospitals = hospitals[i:i+batch_size]

            destinations = [hospital.address for hospital in batch_hospitals]
            matrix = gmaps.distance_matrix(origin, destinations)

            # Check if the response has the expected structure
            if 'rows' in matrix and matrix['rows']:
                row = matrix['rows'][0]  # Apenas uma única entrada em 'rows'

                if 'elements' in row and row['elements']:
                    for hospital, element in zip(batch_hospitals, row['elements']):
                        distance = element.get('distance', {}).get('text', 'N/A')
                        duration = element.get('duration', {}).get('text', 'N/A')

                        if distance == 'N/A' or duration == 'N/A':
                            hospital.distance_from_current_pacient = math.inf
                            hospital.duration_from_current_pacient = math.inf
                        else:
                            hospital.distance_from_current_pacient = distance
                            hospital.duration_from_current_pacient = duration
                else:
                    for hospital in batch_hospitals:
                        hospital.distance_from_current_pacient = math.inf
                        hospital.duration_from_current_pacient = math.inf
            else:
                raise ValueError("Unexpected response structure from Google Maps API.")
    except googlemaps.exceptions.ApiError as e:
        raise ValueError(f"Error from Google Maps API: {str(e)}")