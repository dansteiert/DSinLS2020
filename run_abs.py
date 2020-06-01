import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib import animation, rc
# from IPython.display import HTML

warnings.simplefilter('ignore')

if not os.path.isdir("Plots"):
    os.makedirs("Plots")

from covid_abs.abs import *
from covid_abs.graphics import *

sim = Simulation(
    # Percentage of infected in initial population
    initial_infected_perc = 0.05,
    # Percentage of immune in initial population
    initial_immune_perc = 0.00,
    # Length of simulation environment
    length=100,
    # Height of simulation environment
    height=100,
    # Size of population
    population_size=100,
    # Minimal distance between agents for contagion
    contagion_distance=2.,
    # Maximum percentage of population which Healthcare System can handle simutaneously
    critical_limit=0.05,
    # Mobility ranges for agents, by Status
    amplitudes = {
        Status.Susceptible : 5,
        Status.Recovered_Immune : 5,
        Status.Infected : 5
        },
    preexisting_condition=1.5, # remove addition choose 1
    supermarked=3, # remove addition choose 0
    incubation_period=6 # remove addition choose 0

)

anim = execute_simulation(sim, iterations=40)

#rc('animation', html='jshtml')
rc('animation', html='html5')
# plt.show()
# anim

anim.save(filename=os.path.join("Plots", 'do_nothing.gif'), fps=3)