"""
  Program: Calculator
  Author: Penny
"""


import re

print('Magical Calculator')
print('Type "quit" to exit \n')

previous = 0
run = True

def performMath():
  global run
  global previous
  equation = ''

  #if the user has a previous calculation, use that as prompt
  if previous == 0:
    equation = input('Enter equation: ')
  else:
    equation = input(str(previous))

  #if the user quits
  if equation == 'quit':
    print('Goodbye~')
    run = False
  else:
    equation = re.sub('[a-zA-Z, :()"]', '', equation)  #removed letters to keep things safe
    
    if previous == 0:
      previous = eval(equation)
    else:
      previous = eval(str(previous) + equation)

while run:
  performMath()