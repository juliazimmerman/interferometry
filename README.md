# Radio Interferometry Visibility Simulator

## Description
The Radio Interferometry Visibility Simulator is a Python-based simulator. Centered around the Astropy package, it calculates time, location, and sky coordinates to compute the visibility from sources in the sky that you have inputted. The simulator uses many visibilities to calculate the resulting interference pattern, and uses unpolarized point sources at monochromatic frequencies.

The layout of the simulation:
1. `methods.py` - contains the functions/methods that are used in the simulation.
2. `run_sim.py` - runs the simulation and saves visibility output to a data file.
3. `test_freq_axis.py` - takes the data file and creates a matplotlib plot.

To actually obtain the results / use the simulation, you only need to access the `run_sim.py` and `test_freq_axis.py` files. If you'd like to see the behind-the-scenes work to get the simulation running, look at the `methods.py` file's code!

## Setting up a Virtual Environment
It is recommended to install Astropy in a virtual environment. You can follow the process below to create and activate a Python virtual environment:

```
python3 -m venv RadioInterferometer
source RadioInterferometer/bin/activate
```

## Prerequisites
You will need the following Python packages to run the simulation and obtain the time frequency analysis results:
- numpy
- astropy
- matplotlib
- scipy

Use the process below to install all needed packages.

```
pip install numpy astropy matplotlib scipy
```

## Clone the repository
To get the program and all related files installed on your computer, run the following command to clone the repository:

```
git clone git@github.com:juliazimmerman/interferometry.git
cd interferometry
```

## Running the simulation

To run the simulation, first execute the following command to generate the visibility data:

```
python3 run_sim.py
```

As mentioned above, this is the actual simulation file. Running this step runs the core simulation, and it generates the visibility data into a file named `main_data_output.npy`. The data from this file will be used to create your plot. This file will be saved in your directory.

Next, we will generate the geometric time delay plot. To do so, you must have the visibility data available on your computer as this program will pull from that file, which is why we run the command above before this one. To actualy generate the geometric time delay plot, use the following command:

```
python3 test_freq_axis.py
```
This will create a plot of the geometric time delay of 24 sources instantiated in the sky. This data was simulated by measuring 100,000 frequencies spaced 100kHz apart with 1 baseline (2 antennas, the distance between them is called a baseline). The geometric time delay is in reference to how depending on your antenna positions, one antenna receives data faster than the other. That is called the geometric time delay. This graph helps us model that.

Note: The plot will be saved in the directory as `outputs_geometric_delay.pdf`. Navigate to your directory and open the file to see the plot!

In short, `run_sim.py` is what holds your data and preps it so that it can be used to generate the plot. `test_freq_axis.py` is what actually generates the plot.

Currently, the simulation has parameters already put in place. You can view the parameters used for this plot in the details panel below. Click on the small arrow on the left to expand. 

<details>
<summary> Data set for geometric time delay analysis, as inputted in the program (click to expand)</summary>

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

## Customizing the simulation
If you'd like to customize the simulation to simulate different conditions such as different frequencies, longitude and latitude positions, etc. here's how you can achieve it. This is **not** a command line friendly program. To change the parameters you must change them directly within the Python file itself.

First, open the run_sim.py file. Do this by activating your favorite text editor and accessing this file. 

Next, find line 102. This is the main block that contains all the parameters to generate the data. You can change the values of each variable to anything you wish to simulate different conditions. Make sure to change the values only, not the variables themselves. 

Then, use the following commands to run the simulation again to graph your new data:

```
python3 run_sim.py
python3 test_freq_axis.py
```

## Accessing methods.py
To see the behind-the-scenes work, run the following command:

```
python3 methods.py
```

## Notes
run_sim.py MUST be run first for test_freq_axis.py plot to work. If not, the plot will not generate as the file of output data that the plot is based off will not exist.
