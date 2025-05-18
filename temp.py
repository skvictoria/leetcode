import numpy as np
import matplotlib.pyplot as plt

# Redefine the function z = 2x + y with y fixed at 1
def f(x):
    return x*x + x + 1

# Create a grid of x values
x = np.linspace(-2, 2, 400)
z = f(x)

# Create a new figure for plotting
fig, ax = plt.subplots()

# Plot the line on the xz-plane (y=1)
ax.plot(x, z, color='red')

# Mark the point (1,3) where z = 2*1 + 1
#ax.scatter(1, f(1), color='blue', s=50)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_title('Plot of z=2x+1 with y=1 fixed')

# Show the plot
plt.show()
