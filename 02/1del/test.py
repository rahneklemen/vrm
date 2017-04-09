import numpy as np
from trottersuzuki import *





grid = Lattice2D(256, 15)
# create a 2D lattice


potential = HarmonicPotential(grid, 1, 1)
# define an symmetric harmonic potential with unit frequecy

particle_mass = 1.
hamiltonian = Hamiltonian(grid, potential, particle_mass)
# define the Hamiltonian:
frequency = 1
state = GaussianState(grid, frequency)
# define gaussian wave function state: we choose the ground state of the Hamiltonian
time_of_single_iteration = 1.e-4
solver = Solver(grid, state, hamiltonian, time_of_single_iteration)
# define the solver
# get some expected values from the initial state
print("norm: ", solver.get_squared_norm())
print("Total energy: ", solver.get_total_energy())
print("Kinetic energy: ", solver.get_kinetic_energy())
number_of_iterations = 1000
solver.evolve(number_of_iterations)
# evolve the state of 1000 iterations
# get some expected values from the evolved state
print("norm: ", solver.get_squared_norm())
print("Total energy: ", solver.get_total_energy())
print("Kinetic energy: ", solver.get_kinetic_energy())