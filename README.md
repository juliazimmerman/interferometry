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
python3 -m environment_name.venv
```

To activate the virtual environment (may need to include additional subdirectories depending on where your virtual environment is saved):
```
source environment_name/bin/activate
```
Then, install the packages:

```
pip install numpy, astropy
```


## Running the simulation
The simulation currently has a sample set of data to return a visibility. The data is as follows in the details panel:

<details>
<summary>**Example Data Set as in Program (Click to Expand)**</summary>

The visibility returned by the program is based on the following example input data:

| **Parameter**        | **Value**                                | **Description**                                 |
| :------------------- | :--------------------------------------- | :-----------------------------------------------|
| `amplitude`          | `1`                                      | Unit brightness for all point sources           |
| `time_info`          | `("2025-01-01 00:00:00,", 5, 10)`        | Start time, duration (in hrs), number of points |                      
| `freqs`              | `[100e6, 150e6]`                         | Frequency in Hz                                 |
| `positions_list`     | `[(0, 0, 0), (50, 0, 0)]`                | Antenna cordinates (in meters)                  |
| `source`             | `[(180, 45), (270, 5)]`                  | Two Sources' right ascension and declination    |
| `lon`, `lat`         | `(-118, 45)`                             | Longitude & latitude of antenna array           |

</details>

To run the simulation:
```
python3 run_sim.py
```

Understanding the output:
This will output a list of your 10 time values evenly spaced across 5 hours starting from midnight of January 1st, 2025, your list of frequencies of 100 MHz and 150 MHz, and your calculated baseline array of the two anntenas. It also prints the dimensions of the output array, which in this case is (1, 2, 10) meaning there is 1 baseline, 2 frequencies, and 10 time values. There is a printed message saying, "Each: Row = Frequency, Column = Time, Block = Baseline" to help understand the formatting of the outputed array. Then, the program outputs your visibilities as an array.

Running the simulation also saves two files to your computer, "sample_visibility_inputs.txt" and "sample_visibility_outputs.txt". Both files are a log of the input and output values you inputed and received, allowing you to refer to them in the future. 

## Notes
It's recommended to install astropy in a python virtual environment. Instructions are under "Installation" above.

If you'd like to change the inputs to the simulation to create a new visibility representative of your own data, navigate to line 124, insert the following. Make sure to change the paramters of the main function as well as the name of the visibility_variable to your liking.

```
visibility_variable = main(amplitude, time_info, freqs, positions_list, sources, location_info)
print(visibility_variable)
```



