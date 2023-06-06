#%%
from vpython import *

canvas(title="badminton's movement",width=600, height=600, autoscale=True)

#initial parameter
theta = pi/4 #發射仰角
v0 = 70 #初速
g = vector(0,-9.8,0)
m = 5.50e-3 #羽球重量

#shuttlecock
head = sphere(pos=vector(0,0,0), radius=1.4)
feather = cone(pos=vector(-7,0,0), radius=3.4, axis=vector(7,0,0))

shuttlecock = compound([head,feather], 
                       axis=vector(cos(theta), sin(theta),0), texture=textures.earth, make_trail=True, origin=vector(0,0,0))

#racket
racket_head = cylinder(pos=vector(100,0,0), size=vector(1,29,23))
bat = cylinder(pos=vector(100.5,0,0), radius=0.5, axis=vector(0,-53.5,0))
racket = compound([racket_head,bat], axis=vector(1,0,0), pos=vec(100,0,0), origin=vec(100,-53.5,0), racket_ha = vector(0,0,0))

#parameterze
vel = vector(v0*cos(theta), v0*sin(theta), 0)
w = 10*pi*norm(shuttlecock.axis) #自旋
ww = 50*norm(shuttlecock.axis) #螺線
t = 0
dt = 0.01
T = 100
eta = 1.81e-5 #流體黏滯係數
b = 6*pi*eta*4.33
r = 1

#racket's parameter
ws = 7*vector(0,0,1)

def momentum(m1,v1,m2,v2):
    return None

#TODO: 
# - def force and torque


#%%
while t<T :
    rate(50)

    #spin
    shuttlecock.rotate(axis=norm(shuttlecock.axis), angle=mag(w)*dt) #👍
    # shuttlecock.rotate(axis=norm(vel), origin=norm(cross(vel,g)), angle=mag(ww)*dt)
    

    
    #trajectory
    f = -b*vel
    a = f/m+g
    vel = vel + a*dt
    shuttlecock.pos.x, shuttlecock.pos.y, shuttlecock.pos.z = shuttlecock.pos.x+vel.x*dt, shuttlecock.pos.y+vel.y*dt ,shuttlecock.pos.z+vel.z*dt
    shuttlecock.axis = vel.hat
  
    

    #distance to the plane of racket
    nvector = hat(-racket.axis)
    plane = lambda x, y, z: (nvector.x*x+nvector.y*y+nvector.z*z-(dot(nvector,racket.pos)))/(nvector.x**2+nvector.y**2+nvector.z**2)**0.5
    distance = plane(x=shuttlecock.origin.x,y=shuttlecock.origin.y,z=shuttlecock.origin.z)

    racket.racket_ha = hat(cross(vector(0,0,1),racket.axis))

    # print(distance)
    print(racket.racket_ha)
    if distance>head.radius and distance<20:
        #hit
        racket.rotate(axis=vector(0,0,1), angle=mag(ws)*dt)
    elif distance<head.radius+1:
        break
    
    t += dt


s_rang = dot(shuttlecock.axis,racket.racket_ha) 
#用球拍和球的內積判斷夾角
if s_rang>0:
    print("yes",s_rang)
elif s_rang<0:
    print("no", s_rang)

#我是想說分段寫，要寫進上面迴圈感覺很麻煩🧠
# %%
