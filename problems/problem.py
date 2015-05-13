import sys
import os
sys.path.append(os.path.abspath("."))
from utils.lib import *


"""
:return
  -1 indicates worse
  0 indicates equal
  1 indicates better
"""
def compare(one, two, minimize=True):
  if one == two:
    return 0
  if minimize:
    status = 1 if one < two else -1
  else:
    status = 1 if one > two else -1
  return status

class Decision(O):
  def __init__(i, name, low, high):
    i.name = name
    i.low = low
    i.high = high

  def norm(i, val):
    return norm(val, i.low, i.high)

  def deNorm(i, val):
    return deNorm(val, i.low, i.high)


class Objective(O):
  def __init__(i, name, toMinimize=True, low=None, high=None):
    i.name = name
    i.toMinimize = toMinimize
    i.low = low
    i.high = high
    i.value = None


class Problem(O):
  def __init__(self):
    self.name = ""
    self.desc = ""
    self.decisions = []
    self.objectives = []
    self.evals = 0
    self.population = []
    self.ideal_decisions = None

  def generate(self):
    return [uniform(d.low, d.high) for d in self.decisions]

  def assign(self, decisions):
    for i, d in enumerate(self.decisions):
      d.value = decisions[i]

  def populate(self, n):
    self.population = []
    for _ in range(n):
      self.population.append(self.generate())
    return self.population

  def evaluate(self, decisions=None):
    pass

  def get_ideal_decisions(self, count = 500):
    pass

  def dist(self, one, two):
    pass

  def norm(self, one):
    pass

  """
  Domination is defined as follows:
  for all objectives a in "one" and
  all objectives b in "two"
  every a <= b

  for all objectives a in "one" and
  all objectives b in "two"
  at least one a < b

  Check if one set of decisions ("one")
  dominates other set of decisions ("two")
  """
  def dominates(i, one, two):
    obj1 = one.objectives
    obj2 = two.objectives
    atLeastOnce = False
    for index, (a, b) in enumerate(zip(obj1, obj2)):
      status = compare(a, b, i.objectives[index].toMinimize)
      if status == -1:
        return False
      elif status == 1:
        atLeastOnce = True
    return atLeastOnce