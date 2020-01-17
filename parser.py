import os
import math
from calculator import Calculator

class Parser:
  def __init__(self, calculator):
    self.calculator = calculator

  def parseLine(self, line):
    tokens = line.split()
    self.parseTokens(tokens)

  def parseTokens(self, tokens):
    res = 0.0
    for token in tokens:
      res = self.processToken(token)
    print(res)

  def processToken(self, token):
    if (self.isNumber(token)):
      self.calculator.push(float(token))
    else:
      return self.compute[token](self.calculator)

  def isNumber(self, token):
    try:
      float(token)
      return True
    except ValueError:
      return False

## function dict
  compute = {
    '+': Calculator.add,
    '-': Calculator.substract,
    '*': Calculator.multiply,
    '/': Calculator.divide,
    'sin' : Calculator.sin,
    'clear': Calculator.clear,
    'quit': Calculator.shutdown,
    'help': Calculator.showHelp
  }
