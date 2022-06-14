import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import time

x_len = 1000         # Number of points to display
y_range = [0, 1.1]  # Range of possible Y values to display

dt = 5

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
for i in range(x_len):
    xs.append(i*20/1000)
ys = [0] * x_len
ax.set_ylim(y_range)

# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys)

# Add labels
plt.title('ECG')
plt.xlabel('Temps [s]')
plt.ylabel('Tension [V]')

# This function is called periodically from FuncAnimation
def animate(i, ys):
    temp_c = random.random()
    ys.append(temp_c)

    # Limit y list to set number of items
    ys = ys[-x_len:]

    # Update line with new Y values
    line.set_ydata(ys)

    return line,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,),
    interval=dt,
    blit=True)
plt.show()
