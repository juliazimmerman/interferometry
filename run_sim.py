def main(start, stop, num_times, freq_start, freq_stop, num_freqs, antenna_array, antenna_array_location, source_array):
    return


def main(time_info, freq_info, antenna_info, source_info):

    # construct time_array
    # construct freq_array
    # construct baseline_array
    # maybe construct source array / have it in skycoord

    
    # initially the singular visibility
    compute_visibility()

    # loop through 1 axis
    for i in len(range(freqs)):
        compute_visibility(1,2,3,4,5,5,freqs)

    # loop through 1 axis
    for i in len(range(times)):
        compute_visibility(1,2,3,4,5,5,freqs)


if __name__ == "__main__":
    # 1 time
    time_info = [start, stop, num_times]
    # 1 freq
    freq_info = [start, stop, num_freqs]
    # 2 antennas
    antenna_info = [antenna_array, antenna_array_location]
    # 1 source
    source_info = skycoord_stuff

    main(time_info, freq_info, antenna_info, source_info):
