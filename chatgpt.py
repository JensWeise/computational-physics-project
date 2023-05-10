import math
import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81 # gravitational acceleration
rho = 1.23 # air density
Cd = 0.5 # drag coefficient
A = math.pi * (0.022 / 2) ** 2 # cross-sectional area of the shuttlecock
m = 0.005 # mass of the shuttlecock
S = 6.70e-5 # coefficient of lift force
r = 0.022 # radius of shuttlecock
w = 30 # angular velocity of shuttlecock (rad/s)

# Initial conditions
v0 = 20 # initial velocity
theta0 = math.pi/4 # initial angle with the horizontal
vx0 = v0 * math.cos(theta0)
vy0 = v0 * math.sin(theta0)
x0 = y0 = 0

# Simulation parameters
dt = 0.1 # time step
t_max = 5 # maximum simulation time

# Define functions
def lift_force(v, w):
    return 0.5 * rho * S * (r ** 2) * (v ** 2) * w

def drag_force(v):
    return 0.5 * rho * Cd * A * (v ** 2)

# Initialize arrays
t = np.arange(0, t_max, dt)
x = np.zeros_like(t)
y = np.zeros_like(t)
vx = np.zeros_like(t)
vy = np.zeros_like(t)

# Perform simulation
for i in range(len(t)):
    # Calculate forces
    v = math.sqrt(vx[i] ** 2 + vy[i] ** 2)
    Fg = m * g
    Fl = lift_force(v, w)
    Fd = drag_force(v)
    Fx = -Fd * vx[i] / v
    Fy = -Fd * vy[i] / v + Fg + Fl
    
    # Update velocities and positions
    vx[i+1] = vx[i] + Fx / m * dt
    vy[i+1] = vy[i] + Fy / m * dt
    x[i+1] = x[i] + vx[i+1] * dt
    y[i+1] = y[i] + vy[i+1] * dt
    
    # Apply spin
    spin_angle = w * t[i+1]
    vx[i+1], vy[i+1] = (
        math.cos(spin_angle) * vx[i+1] - math.sin(spin_angle) * vy[i+1],
        math.sin(spin_angle) * vx[i+1] + math.cos(spin_angle) * vy[i+1]
    )

# Plot results
plt.plot(x, y)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()
