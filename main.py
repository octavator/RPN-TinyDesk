import sys
from calculator             import Calculator
from parser                 import Parser
from console_user_interface import ConsoleUserInterface

def main():
  calculator = Calculator()
  parser     = Parser(calculator)
  ui         = ConsoleUserInterface(parser, calculator)
  ui.run()

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
