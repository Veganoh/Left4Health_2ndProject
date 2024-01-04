import os
from dotenv import load_dotenv
import googlemaps

load_dotenv()
api_key = os.getenv("API_KEY")
gmaps = googlemaps.Client(key=api_key)


def duration_to_seconds(duration_str):
    parts = duration_str.split()

    total_seconds = 0
    i = 0
    while i < len(parts):
        try:
            value = int(parts[i])
        except ValueError:
            i += 1
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
        i += 2

    if total_seconds == 0 : return 999999999

    return total_seconds


def calculate_distance_duration(origin, mode, hospitals):
    try:
        batch_size = 25
        result = []

        for i in range(0, len(hospitals), batch_size):
            batch_hospitals = hospitals[i:i + batch_size]
            destinations = [hospital.address for hospital in batch_hospitals]

            matrix = gmaps.distance_matrix(origin, destinations, mode=mode)

            if 'rows' in matrix and matrix['rows']:
                for row in matrix['rows']:
                    elements = row.get('elements', [])
                    for hospital, element in zip(batch_hospitals, elements):
                        duration_str = element.get('duration', {}).get('text', 'N/A')
                        duration_seconds = duration_to_seconds(duration_str)
                        result.append({'ID': hospital.id, 'Duration': duration_seconds})

        result.sort(key=lambda x: x['ID'])
        return result

    except googlemaps.exceptions.ApiError as e:
        raise ValueError(f"Error from Google Maps API: {str(e)}")
