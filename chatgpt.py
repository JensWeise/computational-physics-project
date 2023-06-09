from vpython import *

# Constants
g = vector(0, -9.81, 0) # gravitational acceleration
rho = 1.23 # air density
Cd = 0.5 # drag coefficient
A = pi * (0.022 / 2) ** 2 # cross-sectional area of the shuttlecock
m = 0.005 # mass of the shuttlecock
S = 6.70e-5 # coefficient of lift force
r = 0.022 # radius of shuttlecock
w = 30 # angular velocity of shuttlecock (rad/s)

# Initial conditions
v0 = 20 # initial velocity
theta0 = pi/4 # initial angle with the horizontal
vx0 = v0 * cos(theta0)
vy0 = v0 * sin(theta0)
x0 = y0 = z0 = 0

# Create scene and objects
scene = canvas(title='Badminton Simulation', width=800, height=600, center=vector(0, 1, 0), background=color.white)

racket_head = ellipsoid(pos=vector(100,0,0), lenght=1, width=23, height=29)
bat = cylinder(pos=vector(100,0,0), radius=0.5, axis=vector(0,-53.5,0))
racket = compound([racket_head,bat])
head = sphere(pos=vector(0,0,0), radius=1.4, make_trail=True)
feather = cone(pos=vector(-7,0,0), radius=3.4, axis=vector(7,0,0))

shuttlecock = compound([head,feather], pos=vector(0,0,0), 
                       axis=vector(cos(theta), sin(theta),0))

# Simulation parameters
dt = 0.001 # time step
t_max = 5 # maximum simulation time

# Define functions
def lift_force(v, w):
    return 0.5 * rho * S * (r ** 2) * (v ** 2) * w

def drag_force(v):
    return 0.5 * rho * Cd * A * (v ** 2)

# Perform simulation
t = 0
shuttlecock.velocity = vector(vx0, vy0, 0)
while t < t_max:
    rate(1000)
    
    # Calculate forces
    v = mag(shuttlecock.velocity)
    Fg = m * g
    Fl = lift_force(v, w)
    Fd = drag_force(v)
    F = -Fd * norm(shuttlecock.velocity) + Fg + Fl
    
    # Update velocity and position
    shuttlecock.velocity += F / m * dt
    shuttlecock.pos += shuttlecock.velocity * dt
    
    # Apply spin
    spin_angle = w * t
    shuttlecock.rotate(angle=spin_angle, axis=vector(0, 0, 1))
    
    t += dt
