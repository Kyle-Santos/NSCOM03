# 5.5 Transmission time
bandwidth = 1e6  # Bandwidth in Hz (1 MHz for example)

def transmission_time(message_size):
    """Calculate transmission time given message size."""
    return message_size / bandwidth