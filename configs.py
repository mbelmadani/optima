"""
This file contains configuration of the
problems and optimizers
"""
from __future__ import print_function, division
from utils.lib import O

__author__ = 'panzer'

GENS = 250
REPEATS = 5

def gale_settings():
  """
  Default Settings for GALE
  """
  return O(
    pop_size        = 100,    # Size of Population
    gens            = GENS,   # Number of generations
    allowDomination = True,   # Domination Flag
    gamma           = 0.15    # Gamma factor for mutation
  )

def nsga2_settings():
  """
  Default Settings for NSGA2
  """
  return O(
    pop_size = 100,  # Size of population
    gens = GENS      # Number of generations
  )

def nsga3_settings():
  """
  Default Settings for NSGA3
  """
  return O(
    pop_size = 92,    # Size of Population
    gens = GENS,      # Number of generations
    cr = 1,           # Crossover rate for SBX
    nc = 30,          # eta for SBX
    nm = 20           # eta for Mutation
  )

def de_settings():
  """
  Default Settings for DE
  """
  return O(
    pop_size = 50,    # Size of Population
    gens = GENS,      # Number of generations
    f = 0.75,         # Mutation Factor
    cr = 0.3          # Crossover Rate
  )