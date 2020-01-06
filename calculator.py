import os

class Calculator:
  def __init__(self):
    print("Welcome to Sucaba, your new RPN calculator !\nType 'help' to get all commands and usage")

  def process(self, tokens):
    stack = []
    for token in tokens:
      ret = self.handleToken(token, stack)

      if (ret != 0): # break loop if we received a command
        break
    if (ret == 0): # print result if uninterrupted
      #@TODO: print integer nb w/o '.0'
      print(stack.pop())

  def handleToken(self, token, stack):
    if (self.isOperand(token)):
      return self.doOp(token, stack)
    elif (self.isNumber(token)):
      stack.append(float(token))
      return 0
    else:
      print("An unexpected token was found: %s" % (token))
      return 1

  def doOp(self, token, stack):
    if (len(stack) > 1):
      b = stack.pop()
      a = stack.pop()
      res = self.Ops[token](a, b)
      stack.append(res)
      if (res != None):
        return 0
    else:
      self.Ops[token]()
    return 1

##### UTILS
  def isOperand(self, token):
    if (self.Ops.get(token, '?') != '?'):
      return True
    return False

  def isNumber(self, token):
    try:
      float(token)
      return True
    except ValueError:
      return False

 ##### OPS
  def add(x, y): 
    return x + y

  def substract(x, y): 
    return x - y

  def multiply(x, y): 
    return x * y

  def divide(x, y): 
    return x / y

  # varargs to ignore numbers before command (ex: 2 2 help)
  def clear(*args):
    os.system('cls' if os.name == 'nt' else 'clear')

  def shutdown(*args):
    quit()

  def showHelp(*args):
    print("Type 'quit' to exit this breathtaking program\nType 'clear' to clear your screen\n\
      Note: If the program receives a command, it ignores any other input !\n")

## function dict
  Ops = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide,
    'clear': clear,
    'quit': shutdown,
    'help': showHelp
  }
