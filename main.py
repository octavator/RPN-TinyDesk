from calculator import Calculator

def main():
  calc = Calculator()
  while True:
    ##PYTHON 2 input without evaluating
    userInput = raw_input("RPN Calculator >")
    #(@TODO: arg optionnel -p3)
    ##PYTHON 3
    # userInput = input("RPN Calculator >")
    tokens = userInput.split()
    calc.process(tokens)

if __name__ == "__main__":
    # execute only if run as a script
    main()


##Test inputs
# 20 5 /        =>       4
# 4 2 + 3 -     =>      3
# 3 5 8 * 7 + * =>      141
# 12 3 - 3 / => 3
# -2 3 11 + 5 - * => -18
