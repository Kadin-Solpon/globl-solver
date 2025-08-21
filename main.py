# import json

# file_path = "coordinates_creation\\coords.json"

# file = open(file_path, "r")

# coords = json.load(file)

# print(float(11.1))

from countryinfo import CountryInfo

country = CountryInfo("Serbia")
info = country.info()
print(info["latlng"])  # See what keys are available

# If you want coordinates, you may need to use geopy:
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="geoapi")
# location = geolocator.geocode(f"{info['capital']}, {info['name']}")
# print(location.latitude, location.longitude)