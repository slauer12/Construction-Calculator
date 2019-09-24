import patterns
import switchfunc as sf
incha = 0
inchb = 0
totinch = 0

# Printer extracts and prints out solution.
def printer():
  tft = float(totinch / 12)
  tacres = round(float(tft/43560),4)
  acre = '{} Acres'.format(tacres)
  print(acre)
  print('\n')
  startup()

# Mathmatical functions.
def functions():
  global totinch
  totinch = (incha * inchb)/12
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

def startup():
  global length1, length2
  length1 = ''
  length2 = ''
  length1 = input('Enter length: ')
  sf.funccheck(length1)
  length2 = input('Enter length: ')
  sf.funccheck(length2)
  converter()

startup()