# MassSpringDamper
Code to simulate the dynamics of a single mass attached to a spring and a damper subjected to an external forcing.

## Problem

A block with mass $m$ is attached to a spring ($k$) and a damper ($c$), and is also subject to external forcing, with function $f(t)=\sin{\omega t}$. 

![MassSpringDamperImage](https://github.com/user-attachments/assets/ce52353e-9520-4ec6-add0-d2e105a9f76a)

After some calculations, we get the ODE of this system  

$$m\ddot{x}+c\dot{x}+kx=f \sin{\omega t}$$

Giving the parameters and the appropriate initial conditions, we get the dynamic plot and the phase diagram!

![DynamicsMassSpringDamper](https://github.com/user-attachments/assets/c770c119-5046-4147-8922-9162c921a231)
![PhaseDiagramMassSpringDamper](https://github.com/user-attachments/assets/9412d762-f5bd-4918-a472-10396c5aa56a)

## Input Parameters

$m$ - mass [kg]

$k$ - stiffness [N/m]

$c$ - damping [Ns/m]

$f$ - amplitude of forcing function [N]

$Hz$ - frequency of the forcing function [Hz]
