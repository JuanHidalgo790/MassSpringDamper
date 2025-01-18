# MassSpringDamper
Code to simulate the dynamics of a single mass attached to a spring and a damper subjected to an external forcing

## Problem

A block with mass $m$ is attached to a spring ($k$) and a damper ($c$), and is also subject to external forcing, with function $f(t)=\sin{\omega t}$. 

![MassSpringDamperImage](https://github.com/user-attachments/assets/ce52353e-9520-4ec6-add0-d2e105a9f76a)

The ODE that describes the dynamic of this system is then 

$$m\ddot{x}+c\dot{x}+kx=f \sin{\omega t}$$
