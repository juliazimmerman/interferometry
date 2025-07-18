# All packages used
from astropy.coordinates import EarthLocation, AltAz, SkyCoord
from astropy.time import Time
from astropy import units as u
import numpy as np

# EarthLocation Method
def create_earth_location(lon, lat):
    location = EarthLocation.from_geodetic(lon, lat)
    return location

# Method for creating a single time - use to create only one time object
def set_start_time(time):
    return Time(time)

# Method for creating multiple times - use to create multipe time objects for a time array
# base_time = starting time, x = starting value(string), y = ending value(integer), z = number of points to generate (integer)
def multiple_times(base_time, y, z):
    time_array = Time(base_time) + np.linspace(0, y, z) * u.hour
    for i in range(len(time_array)):
        time_array[i] = Time(time_array[i])
    return time_array

# instantiate point on sky - input arrays like: creating_sky_coordinate([value1, value2], [value1, value2])
def creating_sky_coordinate(ra, dec):
    coordinate = SkyCoord(ra*u.deg, dec*u.deg, frame='icrs')
    return coordinate

# An array to store positions of antennas
def antenna_positions_array(num_of_antennas, positions_list):
    positions_array = np.zeros(shape=(num_of_antennas,3))
    for index, item in enumerate(positions_list):
        positions_array[index, :] = item
    return positions_array

# Calculate the baseline vector
def base_line_vector():
    antenna_array = antenna_positions_array(2, [(50, 0, 0), (0, 100, 0)])
    antenna_1 = antenna_array[0]
    antenna_2 = antenna_array[1]
    b = antenna_2 - antenna_1
    return b

# ŝ Unit Vector Calculation
def unit_vector_calculation():
    # Take variables from previous functions
    icrs_coordinate = creating_sky_coordinate(128, -32.1) # Point on sky
    observation_time = multiple_times('2025-07-18 13:00:00', 6, 10) # Observation Time
    obslocation = create_earth_location(121, 33) # Observation Location
    # Transform our SkyCoord to AltAz then ENU coordinates
    altaz_coordinate = icrs_coordinate.transform_to(AltAz(obstime=observation_time, location=obslocation))
    enu_coordinates = altaz_coordinate.cartesian.xyz.value.T
    return enu_coordinates




