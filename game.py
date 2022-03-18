import random

##defining the function that will print the ASCII art
def choosenOne(c):
  if(c == 0):
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

  elif(c == 1):
    return print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

  elif(c == 2):
    return print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

  else:
      return print("Wrong answer, try again.")
    

##getting the user answer
u = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user = choosenOne(u)

##getting the computer answer randomly
c = random.randint(0,2)
print(f"Computer choice: \n{c}")
computer = choosenOne(c)

##comparing the answers to get the result
if((c == 0 and u == 1) or (u == 0 and c ==2) or (c == 1 and u == 2)):
    print("You win.")

elif((u == 0 and c == 1) or (c == 0 and u ==2) or (u == 1 and c == 2)):
    print("You lose.")

elif(u == c):
    print("It's a tie.")
