#%%
from vpython import *

canvas(title="badminton's movement",width=600, height=600, autoscale=True)

#initial parameter
theta = pi/4 #發射仰角
v0 = 30 #初數
g = vector(0,-9.8,0)
m = 5.50e-3 #羽球重量

#shuttlecock
head = sphere(pos=vector(0,0,0), radius=1.4)
feather = cone(pos=vector(-7,0,0), radius=3.4, axis=vector(7,0,0))

shuttlecock = compound([head,feather], pos=vector(0,0,0), 
                       axis=vector(cos(theta), sin(theta),0), texture=textures.earth, make_trail=True)

#racket
racket_head = ellipsoid(pos=vector(100,0,0), length=1, width=23, height=29)
bat = cylinder(pos=vector(100,0,0), radius=0.5, axis=vector(0,-53.5,0))
racket = compound([racket_head,bat], axis=vector(0,-53.5,0), pos=vec(100,0,0), origin=vec(100,-53.5,0))

#parameter
vel = vector(v0*cos(theta), v0*sin(theta), 0)
w = 10*pi*norm(shuttlecock.axis) #自旋
ww = 50*norm(shuttlecock.axis) #螺線
t = 0
dt = 0.01
T = 100
eta = 1.81e-5 #流體黏滯係數
b = -6*pi*eta*4.33

ws = 10*vector(0,0,1)


#%%
while t<T :
    rate(30)

    #spin
    shuttlecock.rotate(axis=norm(shuttlecock.axis), angle=mag(w)*dt) 
    shuttlecock.rotate(axis=norm(vel), origin=norm(shuttlecock.axis), angle=mag(ww)*dt)
    #swin
    racket.rotate(axis=vector(0,0,1), angle=mag(ws)*dt)
    
    #trajectory
    f = -b*mag(vel)*norm(vel)
    a = f/m+g
    vel = vel + a*dt
    shuttlecock.pos = shuttlecock.pos + vel*dt
    
    
    
    t += dt

# %%
