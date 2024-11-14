# Building the calculator

import sys

def add(num1 , num2):
    add = num1 + num2
    return add

def sub(num1 , num2):
    sub = num1 - num2
    return sub

def multi(num1 , num2):
    multi = num1 * num2
    return multi

def div(num1 , num2):
    div = num1 / num2
    return div

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == 'add':
    print(add(num1 , num2))
elif operation == 'sub':
    print(sub(num1 , num2))
elif operation == 'multi':
    print(multi(num1 , num2))
elif operation == 'div':
    print(div(num1 , num2))