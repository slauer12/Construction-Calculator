import patterns
import switchfunc as sf
incha = 0
inchb = 0
totinch = 0

print('Cubic Yard Calculator')

# Printer extracts and prints out solution.
def printer():
  tyd = round(float(totinch), 2)
  Bag40calc = round(tyd / .011, 1)
  Bag60calc = round(tyd / .017, 1)
  Bag80calc = round(tyd / .022, 1)
  cy = '{} yards'.format(tyd)
  # Bag40 = '{} 40lb bags'.format(Bag40calc)
  # Bag60 = '{} 60lb bags'.format(Bag60calc)
  # Bag80 = '{} 80lb bags'.format(Bag80calc)
  print(cy)
  # print(Bag40)
  # print(Bag60)
  # print('{} \n'.format(Bag80))  
  startup()

# Mathmatical functions.
def functions():
  global totinch
  totinch = (fta * ftb * ftc)/27
  printer()

# Converts lengths into readable format.
def converter(*args):
  global fta, ftb, ftc
  ft1 = patterns.ftbreakdown(length1)
  ft2 = patterns.ftbreakdown(length2)
  ft3 = patterns.ftbreakdown(length3)
  in1 = patterns.inbreakdown(length1)
  in2 = patterns.inbreakdown(length2)
  in3 = patterns.inbreakdown(length3)
  fta = ft1 + (in1/12)
  ftb = ft2 + (in2/12)
  ftc = ft3 + (in3/12)
  functions()

def startup():
  global length1, length2, length3
  length1 = input('Enter length: ')
  sf.funccheck(length1)
  length2 = input('Enter thickness: ')
  sf.funccheck(length2)
  length3 = input('Enter width: ')
  sf.funccheck(length3)
  converter()

startup()