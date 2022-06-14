import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def animate(i, xs, ys):
    temp_c = random.random()

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%M:%S.%f'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-100:]
    ys = ys[-100:]

    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('ECG')
    plt.ylabel('Tension [V]')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)
plt.show()
