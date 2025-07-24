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
def compute_single_visibility(amplitude, obs_freq, positions_list, source, obs_time, location_info):
    # Unpack paramter groups
    lon, lat = location_info

    # Math here
    amplitude_squared = amplitude ** 2
    speed_of_light = c
    v_n = obs_freq
    baseline_vector = base_line_vector(positions_list)
    unit_vector = unit_vector_calculation(source, obs_time, lon, lat)

    dot_product = np.dot(baseline_vector, unit_vector)
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
        for j, freq in enumerate(freq_list):
            for k, time in enumerate(time_list):
                visibility = 0
                for ra, dec in sources:
                    visibility += compute_single_visibility(amplitude, freq, baseline, (ra, dec), time, location_info)
                output_array[i, j, k] = visibility

    # Reshaping the real and imaginary components of the array
    real = output_array.real.reshape(-1)
    imaginary = output_array.imag.reshape(-1)

    # Stack the real and imaginary components side by side
    combined_outputs = np.column_stack((real, imaginary))

    # Save it as a file - each row is 1 visibility, first column is real second column is imaginary.
    #np.savetxt("first_graph_outputs.txt", combined_outputs)
                
    print(f"Output Array: {output_array.shape}")
    print("Each: Row = Frequency, Column = Time, Block = Baseline")

    # Flatten list of tuples
    positions_flattened = np.ravel(position_list)
    sources_flattened = np.ravel(sources)

    # Create Python list of all inputs
    combined_inputs = [amplitude] + list(time_info) + list(freqs) + list(positions_flattened) + list(sources_flattened) + list(location_info)

    # Save into file.
    #np.savetxt("first_graph_inputs.txt", combined_inputs, fmt='%s')

    # The resulting visibility is complex: it stores information on both amplitude and frequency.

    phases = np.angle(visibility)
   
    return output_array



if __name__ == "__main__":

    

    
