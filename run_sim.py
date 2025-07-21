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
    base_time, y, z = time_info # base_time is string of starting time, y is integer for the duration of data, z is inter of number of data points
    time_samples = multiple_times(base_time, y, z)
    return time_samples

# Frequency Array Construction
def freq_array(freqs):
    v_n_array = np.array(freqs)
    return v_n_array

# Baseline Array Construction
def base_line_array(num_of_antennas, positions_list):
    antenna_array = antenna_positions_array(num_of_antennas, positions_list)
    antenna_pairs = []
    for i in range(len(antenna_array)):
        for j in range(i, len(antenna_array)):
            if j != i:
                antenna_pairs.append((i, j))
            else:
                exit
    pair = antenna_pairs[0]
    baseline_list = []
    for pair in antenna_pairs:
        baseline = antenna_array[pair[1]] - antenna_array[pair[0]]
        baseline_list.append(baseline)
    baseline_array = np.array(baseline_list)
    return baseline_array

# Source Array Construction
def source_array(ra, dec):
    list_of_coordinates = creating_sky_coordinate(ra, dec)
    coordinate_array = np.array(list_of_coordinates)
    return coordinate_array

# Calculate Visibility
def compute_visibility(amplitude, freqs, num_of_antennas, positions_list, ra, dec, base_time, y, z, lon, lat):
    amplitude_squared = amplitude ** 2
    complex_exponential = np.exp(2 * np.pi * 1j)
    speed_of_light = c
    v_n = freq_array(freqs)
    baseline_vector = base_line_array(num_of_antennas, positions_list)
    unit_vector = unit_vector_calculation(ra, dec, base_time, y, z, lon, lat)
    dot_product = np.dot(baseline_vector, unit_vector)
    visibility = amplitude_squared * (complex_exponential ** (v_n * (dot_product / speed_of_light)))
    return visibility





