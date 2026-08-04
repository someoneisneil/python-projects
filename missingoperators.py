import random
import time

def spacer():
  for i in range (100):
    print("\n")



spacer()

print("hello to the math test by neil")

time.sleep(3)



num1 = int(input('Please tell me a number\n'))
num2 = int(input('Please tell me another number\n'))

op = random.randint(0, 2)

op_list = ['+', '-', '*']

if op == 0:
  rhs = num1 + num2

if op == 1:
  rhs = num1 - num2

if op == 2:
  rhs = num1 * num2



print('Can you tell me the missing operator\n')
qn = str(num1) + ' __ ' + str(num2) + ' = ' + str(rhs) + '\n'
answer = input(qn)


if answer == op_list[op]:
  print('Well Done')
else: 
  print('pathetic')
  print("the answer was ", op_list[op])

print()
num3 = random.randint(1, 100)



op1 = random.randint(0, 1)
op2 = random.randint(0, 1)


if op1 == 0:
  rhs = num1 + num2

if op1 == 1:
  rhs = num1 - num2

if op2 == 0:
  rhs = rhs + num3

if op2 == 1:
  rhs = rhs - num3


print('Can you tell me the missing operator\n')
qn = str(num1) + ' __ ' + str(num2) + ' __ ' + str(num3) + ' = ' + str(rhs) + '\n'
answer = input(qn)


if answer[0] == op_list[op1] and answer[1] == op_list[op2]:
  print('Well Done')
else: 
  print('pathetic')
  print("the answer was ", op_list[op1],  op_list[op2])