import numpy as np
import matplotlib.pyplot as plt

g=9.81
v0=50
angle=45
theta=np.radians(angle)
vx=v0*np.cos(theta)
vy=v0*np.sin(theta)
t_total=2*(vy)/g
t=np.linespace(0,t_total,num=500)

x=vx+t
y=vy+t-0.5*g*t**2

plt.plot(x,y)
plt.title('projectile motion')
plt.xlable('distance(m)')
plt.ylable('height(m)')
plt.show()
