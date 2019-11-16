#Antonio Diaz, TAMU, antonio.diaz.hsa@tamu.edu, Oct 15, 2019
#Graphing Lorentz Attractor in python
#Ctrl alt N to run code in Visual Studio Code

# Lorentz System of differential Equations: du/dt = sigma * (v - u)
                                       #    dv/dt = rho*u - v - u*w
                                       #    dw/dt = uv - Beta*w
                                       
# numpy allows new mathematical functions
import numpy as np
# scipy integrate allows integration of ODEs
from scipy.integrate import odeint
# matplotlib allows us to import plots
import matplotlib.pyplot as plt
# mplot3d allows us to use 3D graphs.
from mpl_toolkits.mplot3d import Axes3D                     
                         
# setting init values for sigma, beta, rho and init conditions
rho,sigma, beta = 28.0, 10.0, 8.0 / 3.0
u0, v0, w0 = 0, 1, 1.05

# setting max time and number of points
t_max, n = 100, 1000

#defining function from lorenz attractors equations
def f(state, t):
  x, y, z = state  # unpack the state vector
  return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # derivatives

# setting vector init as 1, 1, 1
state0 = [1.0, 1.0, 1.0]
# setting t to go from 0 to 40, at change in t iterations of .1
t = np.arange(0.0, 100.0, 0.01)

# solving for each iteration of states usign odeInt function from scipy
states = odeint(f, state0, t)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(states[:,0], states[:,1], states[:,2])

plt.show()