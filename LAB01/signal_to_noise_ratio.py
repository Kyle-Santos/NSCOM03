# 4.5 Signal to Noise Ratio
import numpy as np

def snr_db(signal_power, noise_power):
    """Calculate SNR in decibels."""
    SNR = signal_power / noise_power
    return 10 * np.log10(SNR)
