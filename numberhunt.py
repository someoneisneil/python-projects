import random 
n = random.randint(1, 100)
print(n)
print('I have selected a number between 1 and 100. Can you guess?')

attempts = 0

done = False

while not done:
  guess = int(input('Guess the number\n'))
    
  attempts = attempts + 1
  
  if guess > n:
    print('My number is smaller than that.\n')
      
  if guess < n:
    print('My number is larger than that.\n')
    
  if guess == n:
    print('Bingo, that is correct.')
    print('You took ', attempts, 'attempts to guess it.')
    done = True

print()
print()

done = False

print("Now it's your chance. You select a number between 1 and 100")
print('Click enter when ready')
perans = input()
auto = input('i can also do it automaticly (Y/N) *plz lowercase:')
print("srry auto in test center fr nw do it manualy")
print("bt u can view test file in this repoitory *the test prjct may fail")
guess = 0
attempts = 0
guess_step = 10; 
prev_answer = 'l'




while not done:
    answer = input('\nIs it '+ str(guess) + '? (y = Yes, s = smaller than that, l = larger than that) \n')
    attempts = attempts + 1 

    if attempts > 1: 
      if answer != prev_answer:
        guess_step = guess_step - 1
      
    prev_answer = answer
  
    if answer.lower() == 's':
        guess = guess - guess_step
    
    if answer.lower() == 'l':
        guess = guess + guess_step
    
    if answer.lower() == 'y':
      print('Bingo, I got it.')
      print('I took ', attempts, 'attempts to guess it.')
      done = True
    
print()
print()

print('I think I can do it faster ')
print('Let me try speed search ')



done = False
low = 0
high = 100
guess_step = 0
attempts = 0

while not done:
    guess = round((low + high)/2)
    answer = input('Is it '+ str(guess) + '? (y = Yes, s = smaller than that, l = larger than that) \n')
    attempts = attempts + 1 

    if answer.lower() == 's':
        high = guess
    
    if answer.lower() == 'l':
        low = guess
    
    if answer.lower() == 'y':
      print('Bingo, I got it.')
      print('I took ', attempts, 'attempts to guess it.')
      done = True
    
print()
print()