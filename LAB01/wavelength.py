# 2.7 Wavelength (Equation)

# Constants
propagation_speed = 3e8  # Speed of light in m/s
bandwidth = 1e6  # Bandwidth in Hz (1 MHz for example)

def wavelength(frequency):
    """Calculate wavelength given frequency."""
    return propagation_speed / frequency
