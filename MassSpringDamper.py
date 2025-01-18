import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

## Single MassSpringDamper System 

###########################################################################################################
# Coded by Juan Andrés Santisteban Hidalgo, PhD
###########################################################################################################
############### Parameters ################################################################################

m = 1               # mass [kg]
k = 10              # stifness [N/m]
c = 5               # damping [Ns/m]

wn = np.sqrt(k/m) / (2 * np.pi) # natural frequency [Hz]

# print(f"The natural frequency is {wn} Hz.")

f = 1                           # forcing function amplitude [N]
Hz = 1.5                        # forcing function frequency [Hz]

omega = Hz*2*np.pi              # forcing function angular frequency [rad/s]

## Simulation time ########################################################################################

t0 = 0                                  # initial time [s]
tf = 20                                 # final time [s]
delta_t = 0.02                          # time step [s]
nt = int(np.round(tf/delta_t))          # number of time steps
tspan = np.linspace(t0, tf, nt)         # time span [s]

## Initial Conditions ######################################################################################
x_0 = 0                                # initial displacement [m]
dx_0 = 0                               # initial velocity [m/s]

X0 = [x_0 , dx_0]                       # initial conditions vector
###########################################################################################################
###########################################################################################################

def vdp1(t, X):

    F = f*np.sin(omega*t)
    DX = np.matmul(np.array([[0, 1], [-k/m, -c/m]]),X)+np.array([0, F/m])
    return np.transpose(DX)

x = np.zeros((len(tspan), len(X0)))   # array for solution
x[0, :] = X0

r = integrate.ode(vdp1).set_integrator("dopri5")  # choice of method
r.set_initial_value(X0, tspan[0])   # initial values
for i in range(1, tspan.size):
   x[i, :] = r.integrate(tspan[i]) # get one more value, add it to the array
   if not r.successful():
       raise RuntimeError("Could not integrate")

# plot of the dynamic response
fig, ax = plt.subplots()
plt.plot(tspan, x[:,0],'r')
ax.set_title('Dynamic Response')
ax.set_xlabel('t [s]')
ax.set_ylabel('x(t) [m]')
ax.grid()
ax.set_axisbelow(True)
# plt.show()

# plot of the phase diagram
fig, ax = plt.subplots()
plt.plot(x[:,0], x[:,1], 'g')
ax.set_title('Phase Diagram')
ax.set_xlabel('x(t) [m]')
ax.set_ylabel('xdot(t) [m/s]')
ax.grid()
ax.set_axisbelow(True)

plt.show()
