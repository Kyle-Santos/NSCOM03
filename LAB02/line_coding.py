# 2.1 Coding Signals: Line Coding (Signal elements vs data element)
import matplotlib.pyplot as plt
import numpy as np

def draw_digital(values, figsize=(6,2), title=""):
    # Create time points for each value
    time = np.linspace(0, 1, len(values))

    fig, ax = plt.subplots(figsize=figsize)

    # Plot the digital signal
    ax.step(time, values, where='mid', linewidth=2, color="red")

    # Adding labels and title
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title(title)

    ax.set_yticks([0, 1])
    ax.set_ylim(-0.5, 1.5)

    plt.show()

# 2.1.1
values = [2, 0, 1, 0, 2]
draw_digital(values)

# 2.1.2
values = [2, 0, 1, 0, 1, 0, 1]
draw_digital(values)

# 2.1.3
values = [1, 0, 1]
draw_digital(values)

# 2.1.4
values = [1, 0, 0.5]
draw_digital(values)

# 4.1
values = [1, 0, 1, 1, 0, 0, 0, 1, -2]
draw_digital(values, (6,1))

# 6.5.1
values = [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1]
draw_digital(values, (6,3))

# 6.5.2
values = [2, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0]
draw_digital(values, (6,3))

# 6.2.1
values = [1, 0, 1, 1, 0, 0, 0, 1] # Digital signal values
draw_digital(values)

# 6.2.2
values = [1, 0, 0, 0, 1, 0, 1, 1] # Digital signal values
draw_digital(values)

# 6.4
values = [0, 0.5, 1, 0.5, 0, 0.5, 0, 0.5, 1, 0.5, 1] # Digital signal values
draw_digital(values)

# 7.1
values = [0.5, 1, 0.5, 0.5, 0, 0.5] # Digital signal values
draw_digital(values)