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
# base_time = starting time, x = starting value, y = ending value, z = number of points to generate
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
def base_line_vector(obsetime=obstime, obsloc=obsloc):
    antenna_array = antenna_positions_array()
    antenna_1 = antenna_array[:, 0]
    antenna_2 = antenna_array[:, 1]
    b = antenna_2 - antenna_1
    return b

# ŝ Unit Vector Calculation
def unit_vector_calculation():
    # Take variables from previous functions
    icrs_coordinate = creating_sky_coordinate() # Point on sky
    observation_time = time_of_observation() # Observation Time
    obslocation = create_earth_location() # Observation Location
    # Transform our SkyCoord to AltAz then ENU coordinates
    altaz_coordinate = icrs_coordinate.transform_to(AltAz(obstime=observation_time, location=obslocation))
    enu_coordinates = altaz_coordinate.cartesian    
    return enu_coordinates)



def main():
    antenna_positions_array()
    unit_vector_calculation()
    base_line_vector()
    check_enucoord_values()
    
if __name__ == "__main__":
    main()


start_time = 12345
end_time = 23456
time_step = 1 * u.hour
num_times = 10

time_array = np.linspace(start_time, end_time, num_times)

# List comprehension: time_array = [Time(time) for time in time_array]

for i in range(len(time_array)):
    time_array[i] = Time(time_array[i])

# Or use this methods
    
for i, time in enumerate(time_array):
    time_array[i] = Time(time)
    # start time, number of time, resolution, end time

    # calcualte

def run_sim()
