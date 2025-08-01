# Radio Interferometry Visibility Simulator

## Description
Python-based simulator that models radio interferometry. Centered around the Astropy package, it calculates time, location, and sky coordinates to compute the visibility from sources in the sky. The simulator uses many visibilities to calculate the resulting interference pattern, and uses unpolarized point sources at monochromatic frequencies.

The layout of the simulation:
1. methods.py - contains the functions/methods that are used in the simulation.
2. run_sim.py - runs the simulation and saves visibility output to a data file.
3. test_freq_axis.py - takes the data file and creates a matplotlib plot.

## Requirements
- Python 3.12.3 was used
- Install following packages:
```
pip install numpy, astropy, matplotlib

## Clone the repo
```
git clone git@github.com:juliazimmerman/interferometry.git
cd interferometry
```

## Creating a virtual environment
It's recommended to install astropy in a virtual environment. To do so:
```
python3 -m venv myenv
```

To activate the virtual environment (may need to include additional subdirectories depending on where your virtual environment is saved):
```
source myenv/bin/activate
```

## Running the simulation

Methods for the simulation is stored in methods.py. If, you would like to take a look at the methods or change something, access the file as follows. This is not required to run the program.
```
python3 methods.py
```

The simulation currently has a set of data to return a set of frequency visibilities for geometric time delay analysis. The data is as follows in the details panel. If you'd like to create a different plot from the geometric time delay analysis, you must open the run_sim.py file and manaully change the inputs to the paramters outlined in the details panel. 

<details>
<summary> Data set for geometric time delay analysis, as in rogram (click to expand)</summary>

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

This creates a file in your directory called "main_data_output.npy".

## Running test_freq_axis.py to generate geometric time delay plot
```
python3 test_freq_axis.py
```

Make sure on line 12 the file name matches the name you saved your visibility data output from run_sim.py on line 113.
## Notes
If you'd like to make any changes to the inputted data, acess run_sim.py's file. There, from line 102 - 109 you can edit the inputs for each variable to configure the simulation to your liking.

run_sim.py MUST be ran first for test_freq_axis.py plot to work. If not, the plot will not generate as the file of output data that the plot is based off will not exist.