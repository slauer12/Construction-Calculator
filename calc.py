import re
incha = 0
inchb = 0
totinch = 0
print('Construction Calculator Version 1.1.0\nType "C" to clear.')

regex = re.compile(r'(?P<feet>[0-9]+\')?\-?(?P<inches>[0-9]+")?')
regexfrac = re.compile(r'(?P<feet>[0-9]+\')?\-?(?P<inches>[0-9]+ [0-9]+/[0-9]+")?')
regexonlyfrac = re.compile(r'(?P<feet>[0-9]+\')?\-?(?P<inches>[0-9]+/[0-9]+")?')
regexdec = re.compile(r'(?P<feet>[0-9]+.[0-9]+\')?\-?(?P<inches>[0-9]+.[0-9]+\")?')

# Search regex for matches in feet
def ftbreakdown(*args):
  for arg in args:
    if '.' not in arg:
      search = regex.search(*args)
      feetsearch = (search.group('feet'))
      feet = int(feetsearch.split("'")[0]) if feetsearch is not None else 0
      return feet
    else:
      # Searches for decimal feet.
      search = regexdec.search(*args)
      feetsearch = (search.group('feet'))
      feet = float(feetsearch.split("'")[0]) if feetsearch is not None else 0
      return feet

# Search regex for matches for inches and fractions of an inch
def inbreakdown(*args):
  for arg in args:
    if '/' not in arg and '.' not in arg:
      # Searches for inches only.
      search = regex.search(*args)
      inchsearch = (search.group('inches'))
      inches = float(inchsearch.split('"')[0]) if inchsearch is not None else 0
      return inches
    elif '/' in arg and ' ' not in arg:
      # Searches for fraction only.
      search = regexonlyfrac.search(*args)
      inchsearch = (search.group('inches'))
      inches = 0
      fracnum = int(inchsearch.split('/')[0])
      fracden = int(inchsearch.split('/')[1].rstrip('"'))
      frac = float(fracnum/fracden)
      inches += frac
      return inches
    elif '.' in arg:
      # Searches for decimal inches.
      search = regexdec.search(*args)
      inchsearch = (search.group('inches'))
      inches = float(inchsearch.split('"')[0]) if inchsearch is not None else 0
      return inches
    else:
      # Searches for inches and fractions of an inch.
      search = regexfrac.search(*args)
      inchsearch = (search.group('inches'))
      inches = int(inchsearch.split(' ')[0]) if inchsearch is not None else 0
      fracstr = (inchsearch.split(' ')[1])
      fracnum = int(fracstr.split('/')[0])
      fracden = int(fracstr.split('/')[1].rstrip('"'))
      frac = float(fracnum/fracden)
      inches += frac
      return inches

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
  ft1 = ftbreakdown(length1)
  ft2 = ftbreakdown(length2)
  in1 = inbreakdown(length1)
  in2 = inbreakdown(length2)
  incha = (ft1 * 12) + in1
  inchb = (ft2 * 12) + in2
  functions()

def looper():
  global operator, length2
  operator = input('Choose operation: ')
  if operator == 'c' or operator == 'C':
    print('\n')
    startup()
  length2 = input('Enter length: ')
  converter()

def startup():
  global length1, length2, operator
  length1 = input('Enter length: ')
  operator = input('Choose operation: ')
  length2 = input('Enter length: ')
  converter()

startup()
