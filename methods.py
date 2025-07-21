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
def multiple_times(base_time, duration, num_of_times):
    time_array = Time(base_time) + np.linspace(0, duration, num_of_times) * u.hour
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
def base_line_vector(antenna1, antenna2):
    b = antenna2 - antenna1
    return b

# ŝ Unit Vector Calculation
# sources is a singular set of ra, dec values like this: (ra, dec)
def unit_vector_calculation(sources, base_time, duration, num_of_times, lon, lat):
    # Take variables from previous functions
    icrs_coordinate = creating_sky_coordinate(ra, dec)
    observation_time = multiple_times(base_time, duration, num_of_times)
    obslocation = create_earth_location(lon, lat)
    # Transform our SkyCoord to AltAz then ENU coordinates
    altaz_coordinate = icrs_coordinate.transform_to(AltAz(obstime=observation_time, location=obslocation))
    enu_coordinates = altaz_coordinate.cartesian.xyz.value.T
    return enu_coordinates[0]


