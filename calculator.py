import os
import math

class Calculator:
  def __init__(self):
    self.operands = []

  def push(self, number): 
    self.operands.append(number)

  def add(self): 
    operand2 = self.operands.pop()
    operand1 = self.operands.pop()
    result =  operand1 + operand2
    self.operands.append(result)
    return result

  def substract(self): 
    operand2 = self.operands.pop()
    operand1 = self.operands.pop()
    result =  operand1 - operand2
    self.operands.append(result)
    return result

  def multiply(self): 
    operand2 = self.operands.pop()
    operand1 = self.operands.pop()
    result =  operand1 * operand2
    self.operands.append(result)
    return result

  def divide(self): 
    operand2 = self.operands.pop()
    operand1 = self.operands.pop()
    result =  operand1 / operand2
    self.operands.append(result)
    return result

  def sin(self): 
    operand = self.operands.pop()
    result =  math.sin(operand)
    self.operands.append(result)
    return result

  def clear(self):
    self.operands = []

  def shutdown(*args):
    quit()

  def showHelp(*args):
    print("Type 'quit' to exit this breathtaking program\nType 'clear' to clear your screen\n\
      Note: If the program receives a command, it ignores any other input !\n")
