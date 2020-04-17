import patterns
import switchfunc as sf
incha = 0
inchb = 0
totinch = 0

print('Board Feet Calculator')

# Printer extracts and prints out solution.
def printer():
  tft = round(float(totinch), 4)
  bf = '{} board feet'.format(tft)
  print(bf)
  print('\n')
  startup()

# Mathmatical functions.
def functions():
  global totinch
  totinch = (incha * inchb * inchc)/144
  printer()

# Converts lengths into readable format.
def converter(*args):
  global incha, inchb, inchc
  ft1 = patterns.ftbreakdown(length1)
  ft2 = patterns.ftbreakdown(length2)
  ft3 = patterns.ftbreakdown(length3)
  in1 = patterns.inbreakdown(length1)
  in2 = patterns.inbreakdown(length2)
  in3 = patterns.inbreakdown(length3)
  incha = (ft1 * 12) + in1
  inchb = (ft2 * 12) + in2
  inchc = (ft3 * 12) + in3
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