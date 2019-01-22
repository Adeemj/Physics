GlowScript 2.7 VPython
from visual import *
from visual.graph import *

## Physical constants.
m1 = 1.0 # mass of pendulum
m2 = 1.0
l1 = 1.0 # lendth of pendulum
l2 = 1.0
g = 9.8 # magnitude of graviational field
r = 0.1

gdisplay(x=200,y=400)
fdvstime = gcurve(color=color.white)

## Differential equation for second derivative of theta.
def thetadotdot(theta1,theta2, theta1dot,theta2dot,time):

    pi = 3.14159265359

# The diff eq!
    num1 = -g*(2*m1+m2)*sin(theta1) - m2*g*sin(theta1-2*theta2)-2*sin(theta1-theta2)*m2*(theta2dot*theta2dot*l2+theta1dot*theta1dot*l1*cos(theta1-theta2))
    den1 = l1*(2*m1+m2-m2*cos(2*theta2-2*theta1))
    
    num2 = 2*sin(theta1-theta2)*(theta1dot*theta1dot*l1*(m1+m2)+g*(m1+m2)*cos(theta1)+theta2dot*theta2dot*l2*m2*cos(theta1-theta2))
    den2 = l2*(2*m1+m2-m2*cos(2*theta2-2*theta1))
    
    theta1dotdot =num1/den1
    
    theta2dotdot=num2/den2 
    
    return [theta1dotdot,theta2dotdot]

## Initialize run.
time     = 0.0
tmax     = 3000
dt       = 0.005
theta1    = 1.57
theta2 = 1.57
theta1dot = 0.0
theta2dot = 0.0

## Create visuals.

display(x=800,y=0)

bob1 = sphere(pos=vector(l1*sin(theta1),-l1*cos(theta1),0),radius = r)
bob2 = sphere(pos=vector(l1*sin(theta1)+l2*sin(theta2),-l1*cos(theta1)-l2*cos(theta2),0),radius = r,color=color.green)
rod1 = cylinder(pos=vector(0,0,0),axis=bob1.pos,radius=bob1.radius*0.1)
rod2 = cylinder(pos=bob1.pos,axis=bob2.pos-bob1.pos,radius=bob2.radius*0.1)

while time < tmax:
    rate(200)
    theta1dotdot=thetadotdot(theta1,theta2, theta1dot,theta2dot, time)[0]
    theta2dotdot=thetadotdot(theta1,theta2, theta1dot,theta2dot, time)[1]
    theta1dot = theta1dot + theta1dotdot*dt
    theta2dot = theta2dot + theta2dotdot*dt
    theta1    = theta1 + theta1dot*dt
    theta2    = theta2 + theta2dot*dt
    time     = time + dt
    #updating the positions of objects
    bob1.pos = vector(l1*sin(theta1),-l1*cos(theta1),0)
    rod1.axis = bob1.pos
    bob2.pos = vector(l1*sin(theta1)+l2*sin(theta2),-l1*cos(theta1)-l2*cos(theta2),0)
    rod2.pos = bob1.pos
    rod2.axis= bob2.pos-bob1.pos
    
