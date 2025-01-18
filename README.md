# MassSpringDamper
Code to simulate the dynamics of a single mass attached to a spring and a damper subjected to an external forcing.

## Problem

A block with mass $m$ is attached to a spring ($k$) and a damper ($c$), and is also subject to external forcing, with function $f(t)=\sin{\omega t}$. 

![MassSpringDamperImage](https://github.com/user-attachments/assets/ce52353e-9520-4ec6-add0-d2e105a9f76a)

Thus, the ODE that describes the dynamic of this system is then 

$$m\ddot{x}+c\dot{x}+kx=f \sin{\omega t}$$

With this code, the Runge-Kutta integrator is used and the results are plotted

![DynamicsMassSpringDamper](https://github.com/user-attachments/assets/c770c119-5046-4147-8922-9162c921a231)
![PhaseDiagramMassSpringDamper](https://github.com/user-attachments/assets/9412d762-f5bd-4918-a472-10396c5aa56a)
