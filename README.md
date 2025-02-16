# Quantum-Particle-in-a-1D-Box
This Python script simulates the time evolution of a quantum particle in a 1D infinite potential well using the finite difference method.
Quantum Particle in a 1D Box

This Python script simulates the time evolution of a quantum particle in a 1D infinite potential well using the finite difference method.

Description:
The script solves the time-dependent Schrödinger equation for a particle confined in a box of length L with infinite potential barriers at the edges. It initializes a Gaussian wave packet and evolves it over time using a finite difference approximation.
The animation displays the probability density , which represents the likelihood of finding the particle at a given position over time.

Dependencies:
Python 3
NumPy
Matplotlib

How It Works
Define the spatial domain: The box is discretized into small segments.
Set up initial conditions: A Gaussian wave packet is placed in the well.
Time evolution: The wavefunction is updated using a finite difference method.
Visualization: The probability density is plotted and animated to show how the wave packet moves and evolves.

How to Run
Ensure you have the required dependencies installed. Then, run:
python quantum_particle_box.py

Expected Behavior
The wave packet starts centered in the box.
It moves and spreads over time due to quantum dispersion.

It reflects off the walls and exhibits interference effects.
