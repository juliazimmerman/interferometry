# All packages used
from astropy.coordinates import EarthLocation
from astropy.time import Time
from astropy import units as u
from astropy.coordinates import SkyCoord
import numpy as np

# EarthLocation Method
def create_earth_location():
    lon = 121
    lat = 33
    location = EarthLocation.from_geodetic(lon, lat)
    print(location)

# Time Method
def time_of_observation():
    times = ['2025-07-11T14:33:00']
    observation_time = Time(times)
    print(observation_time)

# SkyCoord Method
def creating_sky_coordinate():
    data = np.loadtxt('stars.csv', delimiter=',', usecols=(1,2), skiprows=1)
    ra = data[0, 0]
    dec = data[0, 1]
    coordinate = SkyCoord(ra*u.deg, dec*u.deg, frame='icrs', obstime=Time([2000, 2010], format ='jyear'))
    print(coordinate)

def main():
    create_earth_location()
    time_of_observation()
    creating_sky_coordinate()

if __name__ == "__main__":
    main()
