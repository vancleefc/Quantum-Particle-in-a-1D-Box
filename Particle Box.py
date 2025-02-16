import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
L = 1.0  # Box length
dx = 0.01  # Spatial step
dt = 0.0001  # Time step
N = int(L / dx)  # Number of spatial points
x = np.linspace(0, L, N)

# Potential (infinite square well)
V = np.zeros(N)

# Initial wavefunction (Gaussian packet)
x0, sigma, k0 = L / 2, 0.1, 10
psi_real = np.exp(-((x - x0) ** 2) / (2 * sigma ** 2)) * np.cos(k0 * x)
psi_imag = np.exp(-((x - x0) ** 2) / (2 * sigma ** 2)) * np.sin(k0 * x)

# Normalize wavefunction
norm = np.trapz(psi_real ** 2 + psi_imag ** 2, x)
psi_real /= np.sqrt(norm)
psi_imag /= np.sqrt(norm)

# Finite difference coefficients
alpha = dt / (2 * dx ** 2)
def update():
    global psi_real, psi_imag
    psi_real[1:-1] -= alpha * (psi_imag[2:] - 2 * psi_imag[1:-1] + psi_imag[:-2])
    psi_imag[1:-1] += alpha * (psi_real[2:] - 2 * psi_real[1:-1] + psi_real[:-2])

def animate(i):
    update()
    line.set_ydata(psi_real ** 2 + psi_imag ** 2)
    return line,

# Plot setup
fig, ax = plt.subplots()
ax.set_xlim(0, L)
ax.set_ylim(0, 1.2 * np.max(psi_real ** 2))
line, = ax.plot(x, psi_real ** 2 + psi_imag ** 2, lw=2)
ani = animation.FuncAnimation(fig, animate, frames=500, interval=10, blit=True)
plt.show()
