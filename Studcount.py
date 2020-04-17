import patterns
import switchfunc as sf
import math
incha = 0
inchb = 0
totinch = 0

print('Stud Count Calculator')

# Printer extracts and prints out solution.
def printer():
  tstuds = '{} studs are needed for a {} wall.'.format(math.ceil(studcount),length1)
  print(tstuds)
  print('\n')
  startup()

# Mathmatical functions.
def functions():
  global studcount
  studcount = (incha/inchstudoc)
  if studcount % 2 == 0:
    printer()
  else:
    studcount = int(studcount) + 1
    printer()
  

# Converts lengths into readable format.
def converter(*args):
  global incha, inchstudoc
  ft1 = patterns.ftbreakdown(length1)
  ft2 = patterns.ftbreakdown(studoc)
  in1 = patterns.inbreakdown(length1)
  in2 = patterns.inbreakdown(studoc)
  incha = (ft1 * 12) + in1
  inchstudoc = (ft2 * 12) + in2
  functions()

def startup():
  global length1, studoc
  length1 = input('Enter length: ')
  sf.funccheck(length1)
  studoc = input('Enter stud on center dimension: ')
  sf.funccheck(studoc)
  converter()

startup()