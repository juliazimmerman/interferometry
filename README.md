# Radio Interferometry Visibility Simulator

## Description
Python-based simulator that models radio interferometry. Centered around the Astropy package, it calculates time, location, and sky coordinates to compute the visibility from sources in the sky. The simulator uses many visibilities to calculate the resulting interference pattern.

## Clone the repo
```
git clone git@github.com:juliazimmerman/interferometry.git
```

## Installation
It's recommended to install astropy in a virtual environment. To do so:
```
python3 -m venv myenv
```

To activate the virtual environment (may need to include additional subdirectories depending on where your virtual environment is saved):
```
source myenv/bin/activate
```
Then, install the packages:

```
pip install numpy, astropy
```


## Running run_sim.py for visibility output
The simulation currently has a the set of data to return a set of frequency visibilities for geometric time delay analysis. The data is as follows in the details panel:

<details>
<summary>Example Data Set as in Program (Click to Expand)</summary>

The visibility returned by the program is based on the following example input data:

| **Parameter**        | **Value**                                | **Description**                                 |
| :------------------- | :--------------------------------------- | :-----------------------------------------------|
| `amplitude`          | `1`                                      | Unit brightness for all point sources           |
| `time_info`          | `("2023-01-01 00:00:00,", 1, 1)`         | Start time, duration (in hrs), number of points |                      
| `freqs`              | `np.asarray([i*1e5 for i in range(0,100000)]) | Frequency in Hz                            |
| `positions_list`     | `[(0, 0, 0), (100, 0, 0)]`               | Antenna cordinates (in meters)                  |
| `source`             | `np.asarray([[lon, 0] for lon in np.linspace(-180, 165, 24)])`|Sources in ICRS frame       |
| `lon`, `lat`         | `(-50.6, 5)`                             | Longitude & latitude of antenna array           |

</details>

To run the simulation:
```
python3 run_sim.py
```

## Running test_freq_axis.py to generate geometric time delay plot
```
python3 test_freq_axis.py
```

Make sure on line 12 the file name matches the name you saved your visibility data output from run_sim.py on line 113.
## Notes
It's recommended to install astropy in a python virtual environment. Instructions are under "Installation" above.

If you'd like to change the inputs to the simulation to create a new visibility representative of your own data, navigate to line 124, insert the following. Make sure to change the paramters of the main function as well as the name of the visibility_variable to your liking.

```
visibility_variable = main(amplitude, time_info, freqs, positions_list, sources, location_info)
print(visibility_variable)
```



