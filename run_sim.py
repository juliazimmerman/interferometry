# Packages used
from astropy.coordinates import EarthLocation, AltAz, SkyCoord
from astropy.time import Time
from astropy import units as u
import numpy as np
from scipy.constants import c

# Methods from methods.py
from methods import multiple_times, antenna_positions_array, base_line_vector, creating_sky_coordinate, unit_vector_calculation

# Time Array Construction
def time_array(time_info):
    base_time, duration, num_of_times = time_info # base_time is string of starting time, y is integer for the duration of data, z is inter of number of data points
    time_samples = multiple_times(base_time, duration, num_of_times)
    return time_samples

# Baseline Array Construction
def base_line_array(positions_list):
    antenna_array = antenna_positions_array(positions_list)
    antenna_pairs = []
    for i in range(len(antenna_array)):
        for j in range(i, len(antenna_array)):
            if j != i:
                antenna_pairs.append((i,j))
    baseline_list = []
    for pair in antenna_pairs:
        baseline = antenna_array[pair[1]] - antenna_array[pair[0]]
        baseline_list.append(baseline)
    baseline_array = np.array(baseline_list)
    return baseline_array

# Source Array Construction
def source_array(sources):
    list_of_coordinates = []
    for ra, dec in sources:
        coord = creating_sky_coordinate((ra, dec))
        list_of_coordinates.append(coord)
    coordinate_array = np.array(list_of_coordinates)
    return coordinate_array

# Calculate Visibility
# make the core method (this one) only take a SINGLE baseline, frequency, time, source and return a singular value
def compute_single_visibility(amplitude, freqs, positions_list, sources, time_info, location_info):
    # Unpack paramter groups
    base_time, duration, num_of_times = time_info
    lon, lat = location_info

    # Math here
    amplitude_squared = amplitude ** 2
    complex_exponential = np.exp(2j * np.pi)
    speed_of_light = c
    v_n = np.array(freqs)
    baseline_vector = base_line_vector(positions_list)
    unit_vector = unit_vector_calculation(sources, time_info, location_info)
    dot_product = np.dot(baseline_vector, unit_vector)
    visibility = amplitude_squared * (complex_exponential ** (v_n * (dot_product / speed_of_light)))
    return visibility


# sources is a tuple of ra and dec pairs,like this: [(ra1, dec1), (ra2, dec2)...]
def compute_visibility(amplitude, freqs, positions_list, sources, time_info, location_info):
    # Unpack parameter groups
    base_time, duration, num_of_times = time_info
    lon, lat = location_info

    # sum of visibilities here
    visibility = 0
    for ra, dec in sources:
        visibility += compute_single_visibility(amplitude, freqs, num_of_antennas, positions_list, (ra, dec), base_time, duration, num_of_times, lon, lat)
    return visibility

def main(amplitude, time_info, freqs, position_list, sources, location_info):
    
    # Creating Time Array
    # base_time, duration, num_of_times = time_info
    # input like this: main(...('2023-01-01 00:00:00', 6, 10)...)

    time_list = time_array(time_info)

    # Creating Frequency List
    # create an array of frequencies, like this: main(...[100e6, 150e6, ...]...)
    freq_list = freqs

    # Creating Baseline Array
    # using a list of positions, input list like this: main(... [(x, y, z), (a, b, c)]...)
    baseline_array = base_line_array(position_list)

    num_baselines = len(baseline_array)
    num_freqs = len(freq_list)
    num_times = len(time_list)

    output_array = np.zeros(shape=(num_baselines, num_freqs, num_times), dtype = complex)

    for i, baseline in enumerate(baseline_array):
        for j, freq in enumerate(freq_list):
            for k, time in enumerate(time_list):
                visibility = 0
                for ra, dec in sources:
                    visibility += compute_single_visibility(amplitude, freq, baseline, time, (ra, dec), location_info)
                output_array[i, j, k] = visibility
                    
    return output_array[i, j, k]

r = main(1, [(0, 0, 0), (100, 0, 0)], [(180, 45)], ("2023-01-01 00:00:00", 2, 3), [100e6, 150e6], (-111.6, 35.2))
print(r)



