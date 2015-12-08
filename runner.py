from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from configs import REPEATS

# Problems
from problems.dtlz1.dtlz1 import DTLZ1

# Optimizers
from algorithms.nsga3.nsga3 import NSGA3
from algorithms.nsga2.nsga2 import NSGA2
from algorithms.gale.gale import GALE
from algorithms.de.de import DE

__author__ = 'panzer'

problems = [
  DTLZ1(3),
  #DTLZ1(5)
]

algorithms = [
  NSGA3
]


for problem in problems:
  print(problem.name)
  for i in range(REPEATS):
    for algo in algorithms:
      print(algo.__name__)
      solutions = algo(problem).run()
      exit()
      # Store and process solutions