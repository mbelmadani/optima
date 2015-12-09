from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from problems.problem import *
from math import sqrt

__author__ = 'panzer'

class ZDT1(Problem):
  """
  No of Decisions = n = 30.
  Range of each input = [0,1]
  Objectives:
    f1(x) = x1
    f2(x) = g(x)(1 - (x1/g(x))**0.5 )
    where g(x) = 1 + 9*(sum_(i = 2 to n) x_i)/ n-1
  """
  def __init__(self):
    Problem.__init__(self)
    self.name = ZDT1.__name__
    self.desc = "No of Decisions = n = 30. \n \
              Range of each input = [0,1] \n \
              Objectives: \n \
              f1(x) = x1 \n \
              f2(x) = g(x)(1 - (x1/g(x))**0.5 ) \n \
              where g(x) = 1 + 9*(sum_(i = 2 to n) x_i)/ n-1"
    self.decisions = [Decision("x"+str(index+1),0,1) for index in range(30)]
    self.objectives = [Objective("f1", True, 0, 100), Objective("f2", True, 0, 100)]
    self.evals = 0
    self.ideal_decisions = None
    self.ideal_objectives = None

  def evaluate(self, decisions):
    g  = 1 + 9 * sum(decisions[1:]) / (len(decisions)-1)
    objectives = [decisions[0], g * (1 - sqrt(decisions[0]/g))]
    return objectives

  def get_pareto_front(self):
    file_name = "problems/zdt/PF/zdt1.txt"
    pf = []
    with open(file_name) as f:
      for line in f.readlines():
        pf.append(map(float,line.replace("\n","").split(",")))
    return pf