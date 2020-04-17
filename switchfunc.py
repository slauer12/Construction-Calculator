def funccheck(a):
  if a == 'SF' or a == 'sf':
    print('\n')
    import SFCalc
  elif a == 'ac' or a == 'AC':
    print('\n')
    import Acreage
  elif a == 'cc' or a == 'CC':
    print('\n')
    import ConstCalc
  elif a == 'BF' or a == 'bf':
    print('\n')
    import BoardFeet
  elif a == 'CY' or a == 'cy':
    print('\n')
    import CubicYards
  elif a == 'SC' or a == 'sc':
    print('\n')
    import Studcount
  elif a == 'H' or a == 'h':
    print('Command Options\n'
      'SF ----> Square Footage Calculator\n'
      'AC ----> Acreage Calculator\n'
      'CC ----> Construction Calculator\n'
      'BF ----> Board Feet Calculator\n'
      'CY ----> Cubic Yard Calculator\n'
      'C  ----> Clear\n'
      'H  ----> Help\n')
  else:
    pass