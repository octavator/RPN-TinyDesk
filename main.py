import os

# not using lambdas so its not re-evaluated on each run of the for item loop

def add(x, y): 
  return x + y

def substract(x, y): 
  return x - y

def multiply(x, y): 
  return x * y

def divide(x, y): 
  return x / y

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
  return

def quitCalc():
  quit()

def printHelp():
  print("Welcome to your new RPN calculator !\nType 'help' to print this help\nType 'quit' to exit this breathtaking program\n\
    Type 'clear' to clear your screen\nNote that program stop evaluating input after text command and discard previous entries.\n")

Ops = {
  '+': add,
  '-': substract,
  '*': multiply,
  '/': divide,
  ##COuld divide or check first token for these 3 instructions (no args + clear stack) if hard to call with dict
  'clear': clear,
  'quit': quitCalc,
  'help': printHelp
}

def handleToken(token, stack):
  if (isOperand(token)):
    return doOp(token, stack)
  elif ((token.lstrip('+-').isdigit())):
    stack.append(float(token))
    return 0
  else:
    print("An unexpected token was found: %s" % (token))
    return 1

def main():
  while True:
    ##PYTHON 2 input without evaluating
    userInput = raw_input("RPN Calculator >")
    ##PYTHON 3
    # userInput = input("RPN Calculator >")
    tokens = userInput.split()
    stack = []
    for token in tokens:
      ret = handleToken(token, stack)

      if (ret != 0):
        stack = []
        break
    if (len(stack) > 0):
      print("result: %s" % stack.pop())

def isOperand(token):
  if (Ops.get(token, '?') != '?'):
    return True
  return False

def doOp(token, stack):
  if (len(stack) > 1):
    b = stack.pop()
    a = stack.pop()
    res = Ops[token](a, b)
    stack.append(res)
  else:
    #Check if can call help with numbers before ("2 3 + help")
    Ops[token]()
    stack = []
    return 1
  return 0
  


if __name__ == "__main__":
    # execute only if run as a script
    main()


##Test inputs
# 20 5 /        =>       4
# 4 2 + 3 -     =>      3
# 3 5 8 * 7 + * =>      141
# 12 3 - 3 / => 3
# -2 3 11 + 5 - * => -18
