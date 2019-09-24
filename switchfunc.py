def funccheck(a):
  if a == 'SF' or a == 'sf':
    print(a+'\n')
    import SFCalc
  elif a == 'ac' or a == 'AC':
    print(a+'\n')
    import Acreage
  elif a == 'cc' or a == 'CC':
    print(a+'\n')
    import ConstCalc
  elif a == 'H' or a == 'h':
    print('Command Options\n'
      'SF ----> Square Footage Calculator\n'
      'AC ----> Acreage Calculator\n'
      'CC ----> Construction Calculator\n'
      'C ----> Clear\n'
      'H ----> Help\n')
  else:
    pass