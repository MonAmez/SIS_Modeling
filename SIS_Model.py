#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:04:39 2022

@author: monamez
"""

import matplotlib.pylab as plt
import sis_infections as si
import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep

N = 100
S = (N-1)
I = N-S

beta = 0.3
alpha = 0.1


susceptible, infected = si.sis_infection(N, S, I, beta, alpha)

fig = plt.figure()
fig.canvas.set_window_title('SIS model')
 
inf_line, =plt.plot(infected, label='I(t)')
sus_line, = plt.plot(susceptible, label='S(t)')

plt.legend(handles=[inf_line, sus_line])

plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.xlabel('T')
plt.ylabel('N')

plt.show()

#USING SIS_INFECTIONS MODULE 
#SIS_NETWORK METHOD:
g = nx.erdos_renyi_graph(10, 0.5)
nx.draw(g,with_labels=True)
plt.show()
t,s,i = si.sis_network(g,.2,100)
print(t,s,i)

#USING EPIDEMICS MODULE
# USING NETWORKX

# Model selection
#model = ep.SISModel(g)

# Model Configuration
#cfg = mc.Configuration()
#cfg.add_model_parameter('beta', 0.01)
#cfg.add_model_parameter('lambda', 0.005)
#cfg.add_model_parameter("fraction_infected", 0.05)
#model.set_initial_status(cfg)

# Simulation execution
#iterations = model.iteration_bunch(200)

#print("MODEL",iterations)


#t,s,i = discrete_sis_network(g,10,1,1,.1,1)
