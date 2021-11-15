#Dylan Olthoff
#CST-305
#Project 5 - Self-Organized Criticality
#Professor Ricardo Citro
#this project will be using the lorenz system to represent the space lost in memory and also show the chaos phenomenon
#imported libraries consist of mpl_toolkits, and numpy, matplotlib
import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D


def lorenz(x, y, z, s, r, b):

    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot
#set variables for the lorenz system
s = 10
r = 34
b = 2.667

#steps
dt = 0.01
num_steps = 10000

# Need one more for the initial values
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values
xs[0], ys[0], zs[0] = (11.8, 4.4, 2.4) # png, jpg, gif

# calculating the partial derivatives
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i],s,r,b)
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

# Plot
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()

#plot the x(t), y(t), z(t) graphs
ts = np.linspace(0, 100.01, 10001)  # Set array for time based on step size
plt.title("x(t) [JPG] - r: " + str(r))  # Set title
plt.xlabel("t - Time")  # time
plt.ylabel("x - JPG")  # x
plt.plot(ts, xs)  # Plots x(t)
plt.show()  # Show plot
plt.title("y(t) [PNG] - r: " + str(r))  # Set title
plt.xlabel("t - Time")  # Sets x label - time
plt.ylabel("y - PNG")  # y
plt.plot(ts, ys)  # Plots y(t)
plt.show()  # Show plot
plt.title("z(t) [GIF] - r: " + str(r))  # Set title
plt.xlabel("t")  # y
plt.ylabel("z - GIF")  #z
plt.plot(ts, zs)  # Plot z(t)
plt.show()  # Show plot


