#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:06:28 2022

@author: monamez


"""

import random
from collections import defaultdict
import numpy as np
import networkx as nx

def sis_infection(N, S, I, beta, alpha):
    susceptible = []
    infected = []
    
    for t in range(1000):
        S = S - (beta*S*I/N) + alpha * I
        I = I + (beta*S*I/N) - alpha * I
        susceptible.append(S)
        infected.append(I)
    return susceptible, infected

def pair_of_lists():
    return [[], []]

def sis_network(G,p, maxtime,infected_num_t0 = 1, infected_t0=False):
    
    #Input Parameters
    #SIS network simulation using networks
    #G: type networkx Graph - a networkx graph
    #p: type float - transmission probability
    #infected_t0 is the starting list of nodes of infected individuals
    #infected_num_t0 is the desired number of infected individuals in case infected_t0 is empty
    #   default param is 1 infected individual in network
    # number of individuals in network
    #time is current time (iteration)
    #maxtime is maximum number of iterations
    
    #Return Parameters
    # S - numpy array of 
    #
    #
    
  if infected_t0 is False:  
    infected_t0 = list(random.sample(G.nodes(), infected_num_t0))
  N = G.number_of_nodes() 
  S = [N-len(infected_t0)]
  I = [len(infected_t0)]
  time = 0
  t=[]
  transmissions = []
  node_history = defaultdict(lambda : ([0], ['S']))
  new_infected = set()
  
  print("infectedt0 list", infected_t0)
  
  for u in infected_t0:
      t.append(0)
      node_history[u] = (t[0], ['I'])
      transmissions.append((t[time],u))
    
  infected = set(infected_t0)

  while time < maxtime:

      infector={}
      for u in infected:
          
          print("NODE: ---",u)
          print("NEIGHBOR 1: ",G.neighbors(u))
          for v in G.neighbors(u):
              val = random.random()
              print("VAL", val)
              print("NEIGHBOR: ", v)
              print("IF CONDITION INFECTED, RAND VAL",infected,val)
              
              if v not in infected and val<p:
                  if v not in new_infected:
                      print("SECOND IF: V", v)
                      new_infected.add(v)
                      infector[v] = [u]
                  else: 
                      infector[v].append(u)
                      
      for v in infector.keys():
          transmissions.append((t[time], random.choice(infector[v]), v))
      next_time = t[time]+1
      
      
      if next_time <= maxtime:
          for u in infected:
              node_history[u]=(next_time,['S'])
              for v in new_infected:
                  node_history[v]=(next_time,['I'])     
      infected = new_infected
      t.append(time)
      S.append(N-len(infected))
      I.append(len(infected))
      time += 1
  return np.array(t), np.array(S), np.array(I)                 
                      
    