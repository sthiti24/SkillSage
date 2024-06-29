from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError


def get_coordinates(city_name, country=None):
    geolocator = Nominatim(user_agent="my_app")

    try:
        if country:
            location = geolocator.geocode(
                f"{city_name}, {country}", exactly_one=True)
        else:
            location = geolocator.geocode(city_name, exactly_one=True)

        if location:
            return location.latitude, location.longitude
        else:
            return None
    except (GeocoderTimedOut, GeocoderServiceError):
        print(
            f"Error: Geocoding service timed out or encountered an error for {city_name}")
        return None
