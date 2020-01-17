import os
import math
from calculator import Calculator
from parser     import Parser

class ConsoleUserInterface:
  def __init__(self, parser, calculator):
    self.parser     = parser
    self.calculator = calculator

  def run(self):
    while True:
      userInput = input("RPN Calculator > ")
      self.parser.parseLine(userInput)
