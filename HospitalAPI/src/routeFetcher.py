import os
from dotenv import load_dotenv
import googlemaps
import math

def duration_to_seconds(duration_str):
    parts = duration_str.split()

    total_seconds = 0
    for i in range(0, len(parts), 3):
        try:
            value = int(parts[i])
        except ValueError:
            continue

        unit = parts[i + 1].lower()
        unit = unit.rstrip('s')

        if 'day' in unit:
            total_seconds += value * 86400
        elif 'hour' in unit:
            total_seconds += value * 3600
        elif 'min' in unit:
            total_seconds += value * 60
        elif 'sec' in unit:
            total_seconds += value

    return total_seconds


def calculate_distance_duration(origin, mode, hospitals):
    load_dotenv()
    api_key = os.getenv("API_KEY")

    gmaps = googlemaps.Client(key=api_key)

    try:
        batch_size = 25
        result = []

        for i in range(0, len(hospitals), batch_size):
            batch_hospitals = hospitals[i:i + batch_size]

            destinations = [hospital.address for hospital in batch_hospitals]
            matrix = gmaps.distance_matrix(origin, destinations, mode=mode)

            if 'rows' in matrix and matrix['rows']:
                row = matrix['rows'][0]

                if 'elements' in row and row['elements']:
                    for hospital, element in zip(batch_hospitals, row['elements']):
                        duration_str = element.get('duration', {}).get('text', 'N/A')

                        if duration_str == 'N/A':
                            hospital.duration_from_current_pacient = math.inf
                        else:
                            hospital.duration_from_current_pacient = duration_to_seconds(duration_str)

                        result.append({'ID': hospital.id, 'Duration': hospital.duration_from_current_pacient})

                else:
                    for hospital in batch_hospitals:
                        hospital.duration_from_current_pacient = math.inf
                        result.append({'ID': hospital.id, 'Duration': hospital.duration_from_current_pacient})
            else:
                raise ValueError("Unexpected response structure from Google Maps API.")
    except googlemaps.exceptions.ApiError as e:
        raise ValueError(f"Error from Google Maps API: {str(e)}")

    result.sort(key=lambda x: x['ID'])

    return result
