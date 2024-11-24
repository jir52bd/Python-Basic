import numpy as np
import matplotlib.pyplot as plt

# Generate x values (in degrees) from 0 to 180 with steps of 15 degrees
x = np.arange(0, 361, 15)

# Convert degrees to radians
x_rad = np.radians(x)

# Calculate y values (sin(x))
y = np.sin(x_rad)

# Create the plot
plt.plot(x, y, marker='o')

# Add title and labels
plt.title("Graph of y = sin(x)")
plt.xlabel("x (degrees)")
plt.ylabel("y = sin(x)")

# Show grid
plt.grid(True)

# Show the plot
plt.show()
