#%%
from vpython import *

canvas(title="badminton's movement",width=600, height=600, autoscale = False)

#initial parameter
theta = pi/4 #發射仰角
v0 = 50
g = vector(0,-9.8,0)
m = 5.50e-3

#shuttlecock
head = sphere(pos=vector(0,0,0), radius=1.4)
feather = cone(pos=vector(-7,0,0), radius=3.4, axis=vector(7,0,0))

shuttlecock = compound([head,feather], pos=vector(0,0,0), 
                       axis=vector(cos(theta), sin(theta),0), texture=textures.earth, make_trail=True)

#racket
racket_head = ellipsoid(pos=vector(100,0,0), length=1, width=23, height=29)
bat = cylinder(pos=vector(100,0,0), radius=0.5, axis=vector(0,-53.5,0))
racket = compound([racket_head,bat])

#parameter
vel = vector(v0*cos(theta), v0*sin(theta), 0)
w = 10*pi*norm(shuttlecock.axis) #angular velocity
t = 0
dt = 0.01
T = 100
eta = 1.81e-5
b = -6*pi*eta*4.33

#%%
while t<T :
    rate(30)

    #spin
    shuttlecock.rotate(axis=norm(shuttlecock.axis), angle=mag(w)*dt) 
    
    #trajectory
    
        
    f = -b*mag(vel)*norm(vel)
    a = f/m+g
    vel = vel + a*dt
    shuttlecock.pos = shuttlecock.pos + vel*dt
    shuttlecock.axis = norm(vel)
    t += dt