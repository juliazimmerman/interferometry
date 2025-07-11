from astropy.coordinates import EarthLocation
from astropy.time import Time

# EarthLocation
def create_earth_location():
    lat = 33
    lon = 121
    location = EarthLocation.from_geodetic(lon, lat)
    print("EarthLocation: ", location)

create_earth_location()

# Time Object
def time_of_observation():
    times = ['2025-07-11T14:33:00']
    observation_time = Time(times)
    print("Time (in astropy units): ", observation_time)

time_of_observation()
