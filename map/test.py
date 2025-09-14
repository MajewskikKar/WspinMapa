import geopy

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-app")
location = geolocator.reverse("51.009060, 15.643380")

print(location.raw['address']['village'])
