# define variables
a = 1
count = 0

# import random so that the computer can move
import random

# make a banner to display at the start and the end of the game
def displayBanner():
  print("XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO")
  print("O                              X")
  print("X     Noughts and Crosses      O")
  print("O                              X")
  print("XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO")
  print("")
  
# display the banner
displayBanner()

# 2d array which is the board
ox = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]

# display the board
print("  0  1  2")
print(f"0: {ox[0][0]}{ox[0][1]}{ox[0][2]}")
print(f"1: {ox[1][0]}{ox[1][1]}{ox[1][2]}")
print(f"2: {ox[2][0]}{ox[2][1]}{ox[2][2]}")
  
# while loop
while a == 1:
  # player's coordinates
  y = int(input("column number: "))
  x = int(input("row number: "))

  # ensures that the values are integers which are between 0 and 2 (avoid IndexError)
  while ((x != 0 and x !=1 and x !=2) or
         (y != 0 and y != 1 and y !=2)):
    print("Please enter a value between 0 and 2 for both numbers.")
    y = int(input("column number: "))
    x = int(input("row number: "))
    
  # checks that the square is not taken
  while ox[x][y] != "-":
    print("This square is taken.")
    y = int(input("column number: "))
    x = int(input("row number: "))
    
  # player move  
  ox[x][y] = "X"

  # computer coordinates
  y = random.randint(0,2)
  x = random.randint(0,2)
  
  # checks that the square is not taken
  while ox[x][y] != "-":
    y = random.randint(0,2)
    x = random.randint(0,2)
    
  # computer move
  ox[x][y] = "O"

  # display the board
  print("  0  1  2")
  print(f"0: {ox[0][0]}{ox[0][1]}{ox[0][2]}")
  print(f"1: {ox[1][0]}{ox[1][1]}{ox[1][2]}")
  print(f"2: {ox[2][0]}{ox[2][1]}{ox[2][2]}")

  # You Won
  if ox[0][0] == "X" and ox[0][1] == "X" and ox[0][2] == "X":
    print("you won")
    a = 2

  elif ox[0][0]== "X" and ox[1][0] == "X" and ox[2][0] == "X":
    print("you won")
    a = 2

  elif ox[1][0] == "X" and ox[1][1] == "X" and ox[1][2] == "X":
    print("you won")
    a = 2

  elif ox[0][1]== "X" and ox[1][1] == "X" and ox[2][1] == "X":
    print("you won")
    a = 2

  elif ox[2][0] == "X" and ox[2][1] == "X" and ox[2][2] == "X":
    print("you won")
    a = 2

  elif ox[0][2]== "X" and ox[1][2] == "X" and ox[2][2] == "X":
    print("you won")
    a = 2

  elif ox[0][0] == "X" and ox[1][1] == "X" and ox[2][2] == "X":
    print("you won")
    a = 2

  elif ox[0][2]== "X" and ox[1][1] == "X" and ox[2][0] == "X":
    print("you won")
    a = 2

  # You Lost
  elif ox[0][0] == "O" and ox[0][1] == "O" and ox[0][2] == "O":
    print("you lost 1")
    a = 2

  elif ox[0][0]== "O" and ox[1][0] == "O" and ox[2][0] == "O":
    print("you lost 2")
    a = 2

  elif ox[1][0] == "O" and ox[1][1] == "O" and ox[1][2] == "O":
    print("you lost 3")
    a = 2

  elif ox[0][1]== "O" and ox[1][1] == "O" and ox[2][1] == "O":
    print("you lost 4")
    a = 2

  elif ox[2][0] == "O" and ox[2][1] == "O" and ox[2][2] == "O":
    print("you lost 5")
    a = 2

  elif ox[0][2]== "O" and ox[1][2] == "O" and ox[2][2] == "O":
    print("you lost 6")
    a = 2

  elif ox[0][0] == "O" and ox[1][1] == "O" and ox[2][2] == "O":
    print("you lost 7")
    a = 2

  elif ox[0][2]== "O" and ox[1][1] == "O" and ox[2][0] == "O":
    print("you lost 8")
    a = 2

  # You Drew
  for x in range(0,2):
    for y in range(0,2):
      if ox[x][y] != "-":
        count+=1
      if count == 8 and a != 2:
        print("you drew")

# display the banner
if a == 2:
  displayBanner()
