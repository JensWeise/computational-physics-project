from vpython import *
import numpy as np

# 定义一些常量
g = vector(0, -9.8, 0)  # 重力加速度，单位：m/s^2
rho = 1.225  # 空气密度，单位：kg/m^3
Cd = 0.5  # 阻力系数
A = 0.01  # 弹丸截面积，单位：m^2
m = 0.01  # 弹丸质量，单位：kg
v0 = 100.0  # 初速度，单位：m/s
theta = np.pi / 4  # 发射角度，单位：弧度
omega = 20.0  # 膛线旋转角速度，单位：rad/s
r = 0.01  # 膛线半径，单位：m

# 定义初始位置和速度
pos = vector(0, 0, 0)
vel = vector(v0 * np.cos(theta), v0 * np.sin(theta), 0)

# 创建场景和物体
scene = canvas(title='Bullet Trajectory', width=800, height=600)
floor = box(pos=vector(0, -0.1, 0), size=vector(2, 0.2, 2))
bullet = sphere(pos=pos, radius=1, color=color.red)

# 模拟运动
t = 0
dt = 0.01
while pos.y >= 0:
    rate(10)
    # 计算阻力和膛线力
    v = mag(vel)
    Fd = -0.5 * rho * Cd * A * v * vel
    Fl = m * omega ** 2 * r * cross(vel, vector(0, 0, 1))
    # 计算加速度和速度
    a = (Fd + Fl + m * g) / m
    vel += a * dt
    # 计算位置
    pos += vel * dt
    # 更新物体位置
    bullet.pos = pos
    # 更新时间
    t += dt
