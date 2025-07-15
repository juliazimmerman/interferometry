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
    base_time = Time('2025-07-11T00:00:00')
    set_of_times = np.linspace(-2, 2, 4) * u.hour # Collecting 4 time values from 10pm - 2am
    observation_times = base_time + set_of_times
    print(observation_times)
    return observation_times

# SkyCoord Method - adjust ra and dec parameters for each csv file
def creating_sky_coordinate():
    data = np.loadtxt('stars.csv', delimiter=',', usecols=(1,2), skiprows=1)
    ra = data[:, 0]
    dec = data[:, 1]
    coordinate = SkyCoord(ra*u.deg, dec*u.deg, frame='icrs')
    return coordinate

def antenna_positions_array():
    a = np.zeros(shape=(3,2)) # Change second parameter to number of antennas
    # Syntax: a[row, column] = value. Defaults to 0 without specified value.
    a[0, 1] = 10
    return a

# ŝ Unit Vector Calculation
def unit_vector_calculation():
    # Take variables from previous functions
    icrs_coordinate = creating_sky_coordinate()
    observation_time = time_of_observation()
    obslocation = create_earth_location()
    # Transform our SkyCoord to AltAz then ENU coordinates
    altaz_coordinate = icrs_coordinate.transform_to(AltAz(obstime=observation_time, location=obslocation))
    enu_coordinates = altaz_coordinate.cartesian
    return enu_coordinates

def main():
    antenna_positions_array()
    unit_vector_calculation()
if __name__ == "__main__":
    main()
