# All packages used
from astropy.coordinates import EarthLocation, AltAz, SkyCoord
from astropy.time import Time
from astropy import units as u
import numpy as np

# EarthLocation Method
def create_earth_location():
    lon = 121
    lat = 33
    location = EarthLocation.from_geodetic(lon, lat)
    return location

# Time Method
def time_of_observation():
    times = ['2025-07-11T14:33:00']
    observation_time = Time(times)
    return observation_time

# SkyCoord Method - adjust ra and dec parameters for each csv file
def creating_sky_coordinate():
    data = np.loadtxt('stars.csv', delimiter=',', usecols=(1,2), skiprows=1)
    ra = data[0, 0] 
    dec = data[0, 1]
    coordinate = SkyCoord(ra*u.deg, dec*u.deg, frame='icrs', obstime=Time([2000, 2010], format ='jyear'))
    return coordinate

# ŝ Unit Vector Calculation
def unit_vector_calculation():
    # Take variables from previous functions
    icrs_coordinate = creating_sky_coordinate()
    observation_time = time_of_observation()
    obslocation = create_earth_location()
    # Transform our SkyCoord to AltAz coordinates
    altaz_coordinate = icrs_coordinate.transform_to(AltAz(obstime=observation_time, location=obslocation))
    enu_coordinates = altaz_coordinate.cartesian
    
def main():
    unit_vector_calculation()

if __name__ == "__main__":
    main()
