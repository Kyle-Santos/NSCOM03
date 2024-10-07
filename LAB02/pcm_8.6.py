# 8.6 Coding Signals: PCM (Quantization)
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

def plot_stem_signal(t, sampled_times, sampled_values, original_values, D):
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the sampled values using stem plot
    markerline, stemlines, baseline = ax.stem(sampled_times, sampled_values, basefmt='k-', linefmt='r', use_line_collection=True)
    plt.setp(stemlines, 'linewidth', 1)

    # Adding labels and title
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude (D)')
    ax.set_title('Ideal Sampling')

    # Set y-ticks to match the amplitude range in terms of D
    y_ticks = [-4*D, -3*D, -2*D, -D, 0, D, 2*D, 3*D, 4*D]
    ax.set_yticks(y_ticks)

    # Format y-tick labels to show Ds
    y_tick_labels = [f'{int(tick / D)}D' if tick != 0 else '0' for tick in y_ticks]
    ax.set_yticklabels(y_tick_labels)

    # Set y-axis limits
    ax.set_ylim(-5*D, 5*D)

    # Highlight horizontally in intervals of 1D in alternating colors
    for i, y in enumerate(np.arange(-4*D, 5*D, D)):
        color = 'blanchedalmond' if i % 2 == 0 else 'cornflowerblue'
        ax.fill_between([sampled_times[0], sampled_times[-1]], y - D, y + D, color=color, alpha=0.5, zorder=0)

    # Annotate each point with its original value on the right side
    for x, y, orig_value in zip(sampled_times, sampled_values, original_values):
        ax.annotate(f'{orig_value:.2f}', (x, y), textcoords="offset points", xytext=(10, 0), ha='left')

    # Find the index of the value -6.0 in sampled_values
    indices = np.where(np.isclose(sampled_values, -6.0))[0]
    if indices.size > 0:
        index_of_minus_6 = indices[0]
        time_of_minus_6 = sampled_times[index_of_minus_6]
    else:
        time_of_minus_6 = sampled_times[-1]

    # Set x-axis limits
    ax.set_xlim(0, time_of_minus_6)

    # Show the plot
    plt.show()

# Define the scaling factor D
D = 1.0

# Original sampled values
original_values = [-6.1, 7.5, 16.2, 19.7, 11.0, -5.5, -11.3, -9.4, -6.0]

# Scale the sampled values by D
scaled_sampled_values = [value / 5 for value in original_values]

# Time points for the analog signal
t = np.linspace(0, 2 * np.pi, 100)

# Ideal sampling times
Ts = (2 * np.pi) / len(original_values)  # Sampling period
sampled_times = np.arange(0, 2 * np.pi, Ts)

# Plot the stem signal
plot_stem_signal(t, sampled_times, scaled_sampled_values, original_values, D)

# Calculate normalized PAM values
sampled_values = [-6.1, 7.5, 16.2, 19.7, 11.0, -5.5, -11.3, -9.4, -6.0]
D = 5
normalized_pam_values = [value / D for value in sampled_values]

quantization_levels = np.array([-4, -3, -2, -1, 0, 1, 2, 3, 4])

# Calculate the midpoints of the quantization levels
midpoints = (quantization_levels[:-1] + quantization_levels[1:]) / 2

# Map each midpoint to its corresponding quantization level
quantization_level_map = {}
for i, midpoint in enumerate(midpoints):
    quantization_level_map[midpoint] = i

# Calculate normalized quantized values
normalized_quantized_values = []
for value in normalized_pam_values:
    floor_index = np.searchsorted(quantization_levels, value, side='right') - 1
    ceiling_index = floor_index + 1

    if floor_index < 0:
        floor_value = quantization_levels[0]
    else:
        floor_value = quantization_levels[floor_index]

    if ceiling_index >= len(quantization_levels):
        ceiling_value = quantization_levels[-1]
    else:
        ceiling_value = quantization_levels[ceiling_index]

    normalized_quantized_value = (floor_value + ceiling_value) / 2
    normalized_quantized_values.append(normalized_quantized_value)

# Calculate normalized error
normalized_error = [quant - pam for pam, quant in zip(normalized_pam_values, normalized_quantized_values)]

# Calculate quantization codes
quantization_codes = []
for value in normalized_quantized_values:
  quantization_codes.append(quantization_level_map[value])

# Calculate encoded words
encoded_words = [format(code, '03b') for code in quantization_codes]

# Print the table
print("Point | Normalized PAM | Normalized Quantized | Normalized Error | Quantization Code | Encoded Word")
print("-" * 80)
for i, (pam, quant, error, code, word) in enumerate(zip(normalized_pam_values, normalized_quantized_values, normalized_error, quantization_codes, encoded_words)):
    print(f"{i+1:5} | {pam:14.4f} | {quant:20.4f} | {error:15.4f} | {code:16} | {word}")