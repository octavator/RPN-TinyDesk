import sys
from calculator import Calculator

def main():
  calc = Calculator()
  while True:
    #PYTHON 2.X
    if (len(sys.argv) > 1 and sys.argv[1] == '-p2'):
     userInput = raw_input("RPN Calculator >")
    #PYTHON 3.X
    else:
      userInput = input("RPN Calculator >")

    tokens = userInput.split()
    calc.process(tokens)

if __name__ == "__main__":
    # execute only if run as a script
    main()


## Test inputs
# 20 5 /        =>       4
# 4 2 + 3 -     =>      3
# 3 5 8 * 7 + * =>      141
# 12 3 - 3 / => 3
# -2 3 11 + 5 - * => -18
# 3 2 * 16 + 4 2 * + 7 - => 23
# 3 4 * 4 3 * + 1 1 + * 6 - => 42