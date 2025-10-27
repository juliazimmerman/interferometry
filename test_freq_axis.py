# coding: utf-8
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import blackmanharris
from numpy.fft import fft, ifft, fftshift, ifftshift, fftfreq
from astropy.constants import c
import copy

fig = plt.figure()
ax = plt.gca()

freq_vis = np.load("main_data_output.npy")
freq_vis = freq_vis[0,:,0]

blahar = blackmanharris(100000)
windowed_freq = blahar * freq_vis

baseline = 100 # meters
max_time_delay = baseline / c
max_time_delay = max_time_delay.value

# y
fft_windowed_freq = np.fft.fft(windowed_freq)
shifted_fft_window_freq = np.fft.fftshift(fft_windowed_freq)
# x
shifted_delay_time = np.fft.fftshift(np.fft.fftfreq(100000, d=1e5))

plt.plot(shifted_delay_time, np.abs(shifted_fft_window_freq))

# Plot labels
plt.xlabel("Geometric Time Delay (s)", fontsize=24)
plt.ylabel("Relatie Amplitude", fontsize=24)
plt.title("Geometric Time Delay of 24 Sources", fontsize=46)

to_tick = list(np.linspace(-max_time_delay, max_time_delay, 10))
to_tick = [np.round(tick, 8) for tick in to_tick]
print(to_tick)
to_tick_labels = copy.deepcopy(to_tick)
to_tick_labels[0] = "horizon"
to_tick_labels[-1] = "horizon"
plt.xticks(to_tick, to_tick_labels, fontsize=14)

plt.xlim(-max_time_delay, max_time_delay)
plt.tight_layout()
plt.savefig("outputs_geometric_delay.pdf", dpi=300)
print("Saved figure to outputs_geometric_delay.pdf")
