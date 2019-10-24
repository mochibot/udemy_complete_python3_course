#pep guidelines: drop down 2 lines between code and top of the script

def my_function():
  print('This is my function')

my_function()

def my_dynamic_function(name = 'someone', age = 'unknown'):
  print('This is', name, '. My age is', age)

my_dynamic_function(age = 23, name = 'Blah')

def print_people(*people):
  for person in people:
    print('This person is', person);

print_people('Pikachu', 'Mew', 'Psyduck')

def do_math(num1, num2):
  return num1 + num2

math1 = do_math(5, 2)
math2 = do_math(7, 8)

print(math1, math2)

check = 'McRib'

if check == 'McRib':
  print('That\'s what I want!')
elif check == 'Nuggets':
  print('I\'m okay with that')
else: 
  print('No good')

numbers = [1, 2, 3, 4, 5]

for item in numbers:
  print('the curr number is', item)

run = True
current = 1

while run:
  if current == 20:
    run = False
  else: 
    print(current);
    current += 1