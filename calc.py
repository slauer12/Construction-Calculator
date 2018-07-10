# User input
try:
    fe1 = int(input('Enter feet: '))
except ValueError:
    fe1 = 0
try:
    in1 = int(input('Enter inches: '))
except ValueError:
    in1 = 0
try:
    num1 = int(input('Enter numerator: '))
except ValueError:
    num1 = 0
try:
    den1 = int(input('Enter denominator: '))
except ValueError:
    den1 = 0
operator1 = input('Choose operator: ')
if operator1 == '+' or operator1 == '-' or operator1 == '*' or operator1 == '/':
    pass
else:
    print('Invalid operation. Please try again.')
    operator1 = input('Choose operator: ')
try:
    fe2 = int(input('Enter feet: '))
except ValueError:
    fe2 = 0
try:
    in2 = int(input('Enter inches: '))
except ValueError:
    in2 = 0
try:
    num2 = int(input('Enter numerator: '))
except ValueError:
    num2 = 0
try:
    den2 = int(input('Enter denominator: '))
except ValueError:
    den2 = 0

incha = 0
inchb = 0
inchc = 0
totinch = 0


# Convert feet to inches with initial values
def converter(fe1, in1, fe2, in2):
    global incha
    global inchb
    if num1 == 0 or den1 == 0 and num2 == 0 or den2 == 0:
        incha += ((fe1 * 12) + in1)
        inchb += ((fe2 * 12) + in2)
    elif num2 == 0 or den2 == 0:
        incha += ((fe1 * 12) + in1 + (num1 / den1))
        inchb += ((fe2 * 12) + in2)
    elif num1 == 0 or den1 == 0:
        incha += ((fe1 * 12) + in1)
        inchb += ((fe2 * 12) + in2 + (num2 / den2))
    else:
        incha += ((fe1 * 12) + in1 + (num1 / den1))
        inchb += ((fe2 * 12) + in2 + (num2 / den2))

# Convert secondary feet value to inches
def converter2(fe, inc, num, den):
    global inchc
    if num == 0 or den == 0:
        inchc += (fe * 12) + inc
    else:
        inchc += ((fe * 12) + inc + (num / den))

def printer ():
    # Prints out solution
    global operator
    global inchc
    i = int(totinch)
    j = (totinch - i) * 12
    k = int(j)
    frac1 = (j - k)

    # Fraction ranges to display (currently rounded to nearest 1/16th)
    if frac1 > .015 and frac1 < .09374:
        frac1 = ' 1/16'
    elif frac1 > .09374 and frac1 < .15624:
        frac1 = ' 1/8'
    elif frac1 > .15624 and frac1 < .21874:
        frac1 = ' 3/16'
    elif frac1 > .21874 and frac1 < .28124:
        frac1 = ' 1/4'
    elif frac1 > .28124 and frac1 < .34374:
        frac1 = ' 5/16'
    elif frac1 > .34374 and frac1 < .40624:
        frac1 = ' 3/8'
    elif frac1 > .40624 and frac1 < .46874:
        frac1 = ' 7/16'
    elif frac1 > .46874 and frac1 < .53124:
        frac1 = ' 1/2'
    elif frac1 > .53124 and frac1 < .59374:
        frac1 = ' 9/16'
    elif frac1 > .59374 and frac1 < .65624:
        frac1 = ' 5/8'
    elif frac1 > .65624 and frac1 < .71874:
        frac1 = ' 11/16'
    elif frac1 > .71874 and frac1 < .78124:
        frac1 = ' 3/4'
    elif frac1 > .78124 and frac1 < .84374:
        frac1 = ' 13/16'
    elif frac1 > 0.84374 and frac1 < .90624:
        frac1 = ' 7/8'
    elif frac1 > .90624 and frac1 < .96874:
        frac1 = ' 15/16'
    elif frac1 > .96874:
        k = int(round(j))
        frac1 = ''
    else:
        frac1 = ''

    print("""{}'-{}{}" """.format(i, k, frac1))

    inchc = 0
    operator = input('Choose operator: ')
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        pass
    else:
        print('Invalid operation. Please try again.')
        operator = input('Choose operator: ')

# Initial addition function
def add():
    global totinch
    totinch = (incha + inchb) / 12
    printer()


# Looping addition function
def add2():
    global totinch
    global inchc
    global operator
    totinch += (inchc/12)
    printer()

# Initial subtraction function
def subtract():
    global totinch
    totinch = (incha - inchb) / 12
    printer()

# Looping subtraction function
def subtract2():
    global totinch
    global inchc
    global operator
    totinch -= (inchc/12)
    printer()

# Initial multiplication function
def multiply():
    global totinch
    totinch = (incha * inchb) / 12
    printer()

# Looping multiplication function
def multiply2():
    global totinch
    global inchc
    global operator
    totinch *= (inchc/12)
    printer()

# Initial division function
def division():
    global totinch
    totinch = (incha / inchb) / 12
    printer()

# Looping division function
def division2():
    global totinch
    global inchc
    global operator
    totinch /= (inchc/12)
    printer()

# Operator function selection
if operator1 == '+':
    converter(fe1, in1, fe2, in2)
    add()

elif operator1 == '-':
    converter(fe1, in1, fe2, in2)
    subtract()

elif operator1 == '*':
    converter(fe1, in1, fe2, in2)
    multiply()

elif operator1 == '/':
    converter(fe1, in1, fe2, in2)
    division()

# Looping function directions
while operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == 'cc':
    try:
        fe = int(input('Enter feet: '))
    except ValueError:
        fe = 0
    try:
        inc = int(input('Enter inches: '))
    except ValueError:
        inc = 0
    try:
        num = int(input('Enter numerator: '))
    except ValueError:
        num = 0
    try:
        den = int(input('Enter denominator: '))
    except ValueError:
        den = 0
    converter2(fe, inc, num, den)
    if operator == '+':
        add2()
    elif operator == '-':
        subtract2()
    elif operator == '*':
        multiply2()
    elif operator == '/':
        division2()

