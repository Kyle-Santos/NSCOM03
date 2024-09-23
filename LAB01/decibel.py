# 4.2 Decibel
import numpy as np

def decibel(P1, P2):
    """Calculate decibels given two power levels."""
    return 10 * np.log10(P2 / P1)
