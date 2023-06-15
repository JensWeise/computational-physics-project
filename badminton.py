#%%
#以下參數可以自行設定

from vpython import *

canvas(title="badminton's movement",width=600, height=600, autoscale=True)

#initial parameter
theta = pi/4 #發射仰角
v0 = 70 #初速
g = vector(0,-9.8,0) #重力加速度


#shuttlecock (羽球)
head = sphere(pos=vector(0,0,0), radius=1.4)
feather = cone(pos=vector(-7,0,0), radius=3.4, axis=vector(7,0,0))

shuttlecock = compound([head,feather], 
                       axis=vector(cos(theta), sin(theta),0), texture=textures.earth, make_trail=True, origin=vector(0,0,0), m = 5.50e-3)

#racket (羽球拍)
racket_head = cylinder(pos=vector(100,0,0), size=vector(1,29,23))
bat = cylinder(pos=vector(100.5,0,0), radius=0.5, axis=vector(0,-53.5,0))
racket = compound([racket_head,bat], axis=vector(1,0.2,0), pos=vec(100,0,0), origin=vec(100,-53.5,0), racket_ha = vector(0,0,0), mr = 8.5e-2)

#parameter
vel = vector(v0*cos(theta), v0*sin(theta), 0)
w = 10*pi*norm(shuttlecock.axis) #自旋角速度
#ww = 50*norm(shuttlecock.axis) 螺線
t = 0
dt = 0.01
T = 100
eta = 1.81e-5 #流體黏滯係數
b = 6*pi*eta*4.33 #阻力係數

#racket's parameter
ws = 0.1*vector(0,0,1) #羽球拍旋轉角速度

def momentum(v,ws): #拍子的動量變化
    delta_ms = -cross(hit_length,ws)*racket.mr
    vf = (shuttlecock.m*v+delta_ms)/shuttlecock.m
    return vf, delta_ms

def angular_acceleration(v,ws): #角加速度
    delta_ms = momentum(v,ws)[1]
    tou = cross(1.4e-2*hat(shuttlecock.axis),delta_ms/tt)
    alpha = tou/((2/5)*shuttlecock.m*1.4e-2**2)
    return alpha*0.00001



Rate = 50

#%%
while t<T :
    rate(Rate)

    #spin
    shuttlecock.rotate(axis=norm(shuttlecock.axis), angle=mag(w)*dt) #👍
    # shuttlecock.rotate(axis=norm(vel), origin=norm(cross(vel,g)), angle=mag(ww)*dt)
    

    
    #trajectory
    f = -b*vel
    a = f/shuttlecock.m+g
    vel = vel + a*dt
    shuttlecock.pos.x, shuttlecock.pos.y, shuttlecock.pos.z = shuttlecock.pos.x+vel.x*dt, shuttlecock.pos.y+vel.y*dt ,shuttlecock.pos.z+vel.z*dt
    shuttlecock.axis = vel.hat
  
    

    #distance to the plane of racket 球拍與羽球距離
    nvector = hat(-racket.axis)
    plane = lambda x, y, z: (nvector.x*x+nvector.y*y+nvector.z*z-(dot(nvector,racket.pos)))/(nvector.x**2+nvector.y**2+nvector.z**2)**0.5
    distance = plane(x=shuttlecock.origin.x,y=shuttlecock.origin.y,z=shuttlecock.origin.z)

    racket.racket_ha = hat(cross(vector(0,0,1),racket.axis))


    if distance>head.radius and distance<20:
        #hit
        racket.rotate(axis=vector(0,0,1), angle=mag(ws)*dt)
    elif distance<head.radius+1:
        break
    
    t += dt


t_interval = 0
#接觸時間
tt = 0.001

while t_interval<tt:
    rate(Rate*10)

    racket.rotate(axis=vector(0,0,1), angle=mag(ws)*dt)
    shuttlecock.rotate(origin=racket.origin, axis=vector(0,0,1), angle=mag(ws*dt))

    t += dt
    t_interval += dt


#the length of where the shuttlecock hit to the origin of racket 
length = mag(shuttlecock.origin-racket.origin)
hit_length = (length**2-1.4**2)**0.5*racket.racket_ha
rr = -(shuttlecock.origin-racket.origin)-hit_length


s_rang = dot(shuttlecock.axis,racket.racket_ha) 
vf = momentum(vel,ws)[0]
alpha = angular_acceleration(vel,ws)
omega = vector(0,0,0)
print(alpha)
#用球拍和球的內積判斷夾角
if s_rang>0:
    while t<T:
        rate(Rate)
        shuttlecock.rotate(axis=norm(shuttlecock.axis), angle=-0.5*mag(w)*dt)
        f = -b*vf
        a = f/shuttlecock.m+g
        vf = vf+a*dt
        shuttlecock.pos = shuttlecock.pos+vf*dt
        if abs(mag(shuttlecock.axis.hat-vf.hat)) > 0.1:
            omega += alpha*dt
            shuttlecock.rotate(axis=vector(0,0,1), angle=mag(omega)*dt)
            print(vf)
        else:
            shuttlecock.axis = vf
            continue        
        t += dt
elif s_rang<0:
    while t<T:
        rate(Rate)
        shuttlecock.rotate(axis=norm(shuttlecock.axis), angle=-0.5*mag(w)*dt)
        f = -b*vf
        a = f/shuttlecock.m+g
        vf = vf+a*dt
        shuttlecock.pos = shuttlecock.pos+vf*dt
        if abs(mag(shuttlecock.axis.hat-vf.hat)) > 0.1:
            omega += alpha*dt
            shuttlecock.rotate(axis=vector(0,0,1), angle=-mag(omega)*dt)
            print(vf)
        else:
            shuttlecock.axis = vf
            continue        
        t += dt

# %%
