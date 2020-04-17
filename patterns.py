import re

#Pattern = 4'-6" or 4'6"
regex = re.compile(r'(?P<feet>[0-9]+\')?\-?(?P<inches>[0-9]+")?')
#Pattern = 4'-6 1/2" or 4'6 1/2"
regexfrac = re.compile(r'(?P<feet>[0-9]+\')?\-?(?P<inches>[0-9]+ [0-9]+/[0-9]+")?')
#Pattern = 4'-1/2" or 4'1/2"
regexonlyfrac = re.compile(r'(?P<feet>[0-9]+\')?\-?(?P<inches>[0-9]+/[0-9]+")?')
#Pattern = 5.5' or 5.5"
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