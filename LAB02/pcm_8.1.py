# 8.1 Coding Signals: PCM (Ideal Sampling)
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

def plot_stem_signal(t, sampled_times, sampled_values):
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the sampled values using stem plot
    markerline, stemlines, baseline = ax.stem(sampled_times, sampled_values, basefmt='k-', linefmt='r', use_line_collection=True)
    plt.setp(stemlines, 'linewidth', 1)

     # Interpolate the sampled values for a smoother curve
    f = interp1d(sampled_times, sampled_values, kind='cubic')
    t_new = np.linspace(sampled_times[0], sampled_times[-1], 300)
    y_smooth = f(t_new)

    # Connect the stems with a smooth curve
    ax.plot(t_new, y_smooth, 'k--', linewidth=1)

    # Adding labels and title
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Ideal Sampling')

    # Set y-ticks to match the amplitude range
    ax.set_yticks([-1, 0, 1])

    # Set y-axis limits
    ax.set_ylim(-1.5, 1.5)


    # Show the plot
    plt.show()

sampled_values = [-0.4, 0.4, 0.9, 1, 0.6, -0.15, -0.5, -0.4, -0.2]
# Time points for the analog signal
t = np.linspace(0, 2 * np.pi, 100)

# Ideal sampling times
Ts = (2 * np.pi) / len(sampled_values)  # Sampling period
sampled_times = np.arange(0, 2 * np.pi, Ts)

# Plot the stem signal
plot_stem_signal(t, sampled_times, sampled_values)