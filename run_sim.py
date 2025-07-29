# Packages used
from astropy.coordinates import EarthLocation, AltAz, SkyCoord
from astropy.time import Time
from astropy import units as u
import numpy as np
from scipy.constants import c

# Methods from methods.py
from methods import multiple_times, antenna_positions_array, creating_sky_coordinate, unit_vector_calculation

# Time Array Construction
def time_array(time_info):
    base_time, duration, num_of_times = time_info
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
def compute_single_visibility(amplitude, obs_freq, baseline_vec, source, obs_time, location_info, unit_vector):
    if type(unit_vector) == str:
        return 0+0j

    # Unpack paramter groups
    lon, lat = location_info

    # Math here
    amplitude_squared = amplitude ** 2
    speed_of_light = c
    v_n = obs_freq

    dot_product = np.dot(baseline_vec, unit_vector[[1,0,2]])
    geometric_time_delay = dot_product / speed_of_light

    visibility = amplitude_squared * np.exp(2j * np.pi * v_n * geometric_time_delay)

    return visibility

def main(amplitude, time_info, freqs, position_list, sources, location_info):
    # Creating Time Array
    # base_time, duration, num_of_times = time_info
    # input like this: main(...('2023-01-01 00:00:00', 6, 10)...)

    time_list = time_array(time_info)
    print(f"Time list: {time_list}")

    # Creating Frequency List
    # create an array of frequencies, like this: main(...[100e6, 150e6, ...]...)
    freq_list = freqs
    print(f"Freq list: {freq_list}")

    # Creating Baseline Array
    # using a list of positions, input list like this: main(... [(x, y, z), (a, b, c)]...)
    baseline_array = base_line_array(position_list)
    print(f"Baseline array: {baseline_array}")

    num_baselines = len(baseline_array)
    num_freqs = len(freq_list)
    num_times = len(time_list)

    output_array = np.zeros(shape=(num_baselines, num_freqs, num_times), dtype = complex)

    for i, baseline in enumerate(baseline_array):
        #print(f"baseline {baseline}")
        for k, time in enumerate(time_list):
            unit_vectors = [unit_vector_calculation(source, time, location_info) for source in sources]
            #print(f"unit: {unit_vectors}")
            for j, freq in enumerate(freq_list):
                print(i,j,k)
                visibility = 0
                for l, source in enumerate(sources):
                    visibility += compute_single_visibility(amplitude, freq, baseline, (source[0], source[1]), time, location_info, unit_vectors[l])
                output_array[i, j, k] = visibility
 
    return output_array



if __name__ == "__main__": 
    print("Running Main:")
    amplitude = 1
    freq_array = np.asarray([i*1e5 for i in range(0,100000)])
    time = ("2023-01-01 00:00:00", 1, 1)
    ants = np.asarray([(0,0,0), (100,0,0)])
    ant_loc = (-50.6, 0)
    sources = np.asarray([[lon, 0] for lon in np.linspace(-180, 165, 24)])

    r = main(amplitude, time, freq_array, ants, sources, ant_loc)

    np.save("data_output.npy", r)

