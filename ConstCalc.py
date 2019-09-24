import patterns
import switchfunc as sf
incha = 0
inchb = 0
totinch = 0

# Printer extracts and prints out solution.
def printer():
  global length1
  # tft returns the feet portion as an integer
  tft = int(totinch / 12)
  # tin returns the inch portion as an integer.
  tin = ((totinch/12) - tft) * 12
  # tinf and tfrac return the fraction portion.
  tinf = int(tin)
  tfrac = float(tin-tinf)
  # Converts decimal to fraction for printing out.
  if tfrac < .03125:
    tfrac = ""
  elif tfrac >= .03125 and tfrac < .09375:
    tfrac = ' 1/16'
  elif tfrac >= .09375 and tfrac < .15625:
    tfrac = ' 1/8'
  elif tfrac >= .15625 and tfrac < .21875:
    tfrac = ' 3/16'
  elif tfrac >= .21875 and tfrac < .28125:
    tfrac = ' 1/4'
  elif tfrac >= .28125 and tfrac < .34375:
    tfrac = ' 5/16'
  elif tfrac >= .34375 and tfrac < .40625:
    tfrac = ' 3/8'
  elif tfrac >= .40625 and tfrac < .46875:
    tfrac = ' 7/16'
  elif tfrac >= .46875 and tfrac < .53125:
    tfrac = ' 1/2'
  elif tfrac >= .53125 and tfrac < .59375:
    tfrac = ' 9/16'
  elif tfrac >= .59375 and tfrac < .65625:
    tfrac = ' 5/8'
  elif tfrac >= .65625 and tfrac < .71875:
    tfrac = ' 11/16'
  elif tfrac >= .71875 and tfrac < .78125:
    tfrac = ' 3/4'
  elif tfrac >= .78125 and tfrac < .84375:
    tfrac = ' 13/16'
  elif tfrac >= .84375 and tfrac < .90625:
    tfrac = ' 7/8'
  elif tfrac >= .90625 and tfrac < .96875:
    tfrac = ' 15/16'
  elif tfrac >= .96875:
    tinf += 1
    tfrac = ''
  length1 = """{}'-{}{}" """.format(tft, tinf, tfrac)
  print(length1)
  looper()

# Mathmatical functions.
def functions():
  global totinch
  if operator == "+":
    totinch = (incha + inchb)
  elif operator == "-":
    totinch = (incha - inchb)
  elif operator == "*":
    totinch = (incha * inchb)/12
  elif operator == "/":
    totinch = (incha / inchb)*12
  printer()

# Converts lengths into readable format.
def converter(*args):
  global incha, inchb
  ft1 = patterns.ftbreakdown(length1)
  ft2 = patterns.ftbreakdown(length2)
  in1 = patterns.inbreakdown(length1)
  in2 = patterns.inbreakdown(length2)
  incha = (ft1 * 12) + in1
  inchb = (ft2 * 12) + in2
  functions()

def looper():
  global operator, length2
  operator = input('Choose operation: ')
  sf.funccheck(operator)
  if operator == 'c' or operator == 'C':
    print('\n')
    startup()
  length2 = input('Enter length: ')
  sf.funccheck(length2)
  converter()

def startup():
  global length1, length2, operator
  length1 = input('Enter length: ')
  sf.funccheck(length1)
  operator = input('Choose operation: ')
  sf.funccheck(operator)
  length2 = input('Enter length: ')
  sf.funccheck(length2)
  converter()

startup()