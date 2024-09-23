# 3.2 Broadband Transmission
from scipy.signal import firwin, remez, kaiser_atten, kaiser_beta
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Functions to create bandpass FIR filters

def create_bandpass_firwin(ntaps, lowcut, highcut, fs, window='hamming'):
    return firwin(ntaps, [lowcut, highcut], fs=fs, pass_zero=False, window=window)

def create_bandpass_kaiser(ntaps, lowcut, highcut, fs, width):
    beta = kaiser_beta(kaiser_atten(ntaps, width/(0.5*fs)))
    return firwin(ntaps, [lowcut, highcut], fs=fs, pass_zero=False, window=('kaiser', beta))

def create_bandpass_remez(ntaps, lowcut, highcut, fs, width):
    delta = 0.5 * width
    edges = [0, lowcut - delta, lowcut + delta, highcut - delta, highcut + delta, 0.5*fs]
    return remez(ntaps, edges, [0, 1, 0], fs=fs)

# Main program to create filters and plot their responses
if __name__ == "__main__":
    # Set sample rate and cutoff frequencies
    fs = 100.0  # Changed sample rate
    lowcut = 5.0  # Changed low cutoff frequency
    highcut = 20.0  # Changed high cutoff frequency
    ntaps = 128

    # Create filters
    hamming_taps = create_bandpass_firwin(ntaps, lowcut, highcut, fs)
    kaiser16_taps = create_bandpass_kaiser(ntaps, lowcut, highcut, fs, width=2.0)  # Adjusted width
    kaiser10_taps = create_bandpass_kaiser(ntaps, lowcut, highcut, fs, width=1.5)  # Adjusted width
    remez_taps = create_bandpass_remez(ntaps, lowcut, highcut, fs, width=1.5)  # Adjusted width

    # Plot frequency responses
    plt.figure(figsize=(12, 9))
    plt.fill_between([lowcut, highcut], 0, 1, color="#60ff60", alpha=0.2)

    for taps, label in zip(
        [hamming_taps, kaiser16_taps, kaiser10_taps, remez_taps],
        ["Hamming window", "Kaiser window, width=2.0", "Kaiser window, width=1.5", "Remez algorithm, width=1.5"]
    ):
        w, h = freqz(taps, 1, worN=2000, fs=fs)
        plt.plot(w, abs(h), label=label)

    plt.xlim(0, 30.0)  # Adjusted x-axis limit
    plt.ylim(0, 1.1)
    plt.grid(True)
    plt.legend()
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain')
    plt.title(f'Frequency response of several FIR filters with {ntaps} taps')
    plt.show()
