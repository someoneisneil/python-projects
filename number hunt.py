import random
import time

print("\n" * 100)

n = random.randint(1, 100)
print(n)

time.sleep(0.2)

print("\n" * 10000)

print("I have selected a number between 1 and 100. Can you guess?")

attempts = 0

done = False

while not done:
    guess = input("Guess the number\n")

    if not guess.isdigit():
        print("sorry your answer didnt go through try again")
    else:
        guess = float(guess)    

        if guess > 100:
            print("try again that wasnt inside 1-100")
        else:


            attempts = attempts + 1

            if guess > n:
                print("My number is smaller than that.\n")

            if guess < n:
                print("My number is larger than that.\n")

            if guess == n:
                print("Bingo, that is correct.")
                print("You took ", attempts, "attempts to guess it.")
                done = True




print()
print()

done = False

print("Now it's your chance. You select a number between 1 and 100")
print("Click enter when ready")




def asknum():
    global perans
    
    while True:
        try:
            
            user_input = int(float(input("type your answer here:")))
            
            perans = user_input

            if perans > 100:
                print("sorry that is greater than 100 try again")
                asknum()

            if perans < 0:
                print("sorry that is less than 0 try again")
                asknum()
            break
            
        except ValueError:
            print("sorry your answer didnt go through try again")



asknum()

if perans > 100:
    print("sorry that is greater than 100 try again")
    asknum()

if perans < 0:
    print("sorry that is less than 0 try again")
    asknum()

print("your locked-in number is:", perans)





auto = input("i can also do it automaticly (Y/N):")


guess = 0
attempts = 0
guess_step = 10
prev_answer = [-1,-1]



if auto.lower() == "y":
    answer = 0
    while not done:
        attempts = attempts + 1

        if attempts > 1:
            if prev_answer[-2] == answer:
                guess_step = guess_step - 1

        prev_answer.append(answer)

        if answer < perans:
            print("guess its greater than", answer)
            guess = guess - guess_step
            answer = answer + guess_step

            time.sleep(1)

        elif answer > perans:
            print("guess its less than", answer)
            guess = guess + guess_step
            answer = answer - guess_step

            time.sleep(1)

        elif answer == perans:
            print("guess its exactly", answer)
            time.sleep(3)
            print("Bingo, I got it.")
            time.sleep(2)
            print("I took ", attempts, "attempts to guess it.")
            done = True

else:
  while not done:
      answer = input(
          "Is it "+ str(guess)+ "? (y = Yes, s = smaller than that, l = larger than that) \n")
      attempts = attempts + 1

      if attempts > 1:
          if answer != prev_answer:
              guess_step = guess_step - 1

      prev_answer = answer

      if answer.lower() == "s":
          guess = guess - guess_step

      if answer.lower() == "l":
          guess = guess + guess_step

      if answer.lower() == "y":
          print("Bingo, I got it.")
          print("I took ", attempts, "attempts to guess it.")
          done = True

print()
print()

print("I think I can do it faster ")
print("Let me try speed search ")


done = False
low = 0
high = 100
guess_step = 0
attempts = 0

while not done:
    guess = round((low + high) / 2)
    answer = input("Is it "+ str(guess)+ "? (y = Yes, s = smaller than that, l = larger than that) \n")
    attempts = attempts + 1

    if answer.lower() == "s":
        high = guess

    if answer.lower() == "l":
        low = guess

    if answer.lower() == "y":
        print("Bingo, I got it.")
        print("I took ", attempts, "attempts to guess it.")
        done = True

print()
print()
