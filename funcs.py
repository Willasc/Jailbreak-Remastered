#imports
import time
import random
import string
import sys
import os   #From https://www.scaler.com/topics/how-to-clear-screen-in-python/


global username
global paperclip

#funcs - choices, events etc
def startup():
  global username
  print("       _         _____ _      ____  _____  ______          _  __\n      | |  /\   |_   _| |    |  _ \|  __ \|  ____|   /\   | |/ /\n      | | /  \    | | | |    | |_) | |__) | |__     /  \  | ' / \n  _   | |/ /\ \   | | | |    |  _ <|  _  /|  __|   / /\ \ |  <  \n | |__| / ____ \ _| |_| |____| |_) | | \ \| |____ / ____ \| . \ \n  \____/_/    \_\_____|______|____/|_|  \_\______/_/    \_\_|\_\\                                                                ")
  time.sleep(3)
  username = input("Enter username: ")
  input(f"Hello {username}, press enter to continue.")
  time.sleep(1)
  os.system("clear")   #From https://www.scaler.com/topics/how-to-clear-screen-in-python/
  time.sleep(2)
  return username
  
def intro(username):
  print(f"YOU AWAKE TO FIND A NOTE ON YOUR BED\n====================================\nDear {username},\n\nWelcome to New Haven penetentary, the best low security prison\nin the world. I wish you a happy stay and that you return to society in no time!\n\nIf you get bored of the free to air TV, perhaps try an activity thoughout the facility!\n\nKind regards,\n\n\nWarden William Colquhoun.\n\n")

def gameover(username):
  print(f"GAME OVER, {username}.")
  time.sleep(1)
  restart = input("Would you like to restart?\ny/n?: ")
  while not (restart == "y" or restart == "n"):
    print("Invalid input.")
    restart = input("Would you like to restart? (y/n): ")
  if restart == "y":
    os.system("clear")
    os.execl(sys.executable, sys.executable, *sys.argv)
  elif restart == "n":
    exit()

def cell1():
  choice = input("What would you like to do?\n(a) Inspect the cell\n(b) Look under the bed\n")
  while not (choice == "a" or choice == "b"):
    print("Invalid input.")
    time.sleep(1)
    choice = input("What would you like to do?\n(a) Inspect the cell\n(b) Look under the bed\n")
  if choice == "a":
    print("You look around your cell. You think it will be good to think about a way of escaping at lunchtime.")
    lunchtime()
    time.sleep(3)
  elif choice == "b":
    print("\nUnder the bed you find a paperclip.")
    time.sleep(1)
    print("\nWould you like to take the paperclip?")
    paperclip = input("y/n?: ")
    while not (paperclip == "y" or paperclip == "n"):
      print("Invalid input.")
      time.sleep(1)
      paperclip = input("y/n?: ")
    if paperclip == ("y"):
      paperclip = True
      time.sleep(1)
      print("You take the paperclip.")
      picklock()
    if paperclip == ("n"):
      print("You don't bother to pick up the paperclip. Not like it would be useful or anything...")
      time.sleep(3)
      lunchtime()

def lunchtime():
  os.system("clear")
  print("You decided to wait until it is lunch time.")
  time.sleep(3)
  os.system("clear")
  time.sleep(1)
  print("LUNCH TIME\n==========\n\n")
  time.sleep(2)
  print("At lunch time, you and the other inmates sit eating.")
  choice = input("Would you like to start a riot?\n(y/n): ")
  while not (choice == "y" or choice == "n"):
    print("\n\nInvalid input.")
    time.sleep(1)
    choice = input("Would you like to start a riot in attempt to escape?\n(y/n): ")
  if choice == "y":
    os.system("clear")
    print("RIOT\n====")
    time.sleep(2)
    print("\n\nYou jump up on the table and shout at your fellow inmate to join you in trying to break out.")
    chance = random.randint(1,3)
    time.sleep(3)
    if chance == 1:
      print("There is an awkward silence as everyone looks at you. A guard comes and drags you back to your cell")
      gameover()
    elif chance == 2:
      print("Your fellow inmates agree and charge at the guards, taking them down. They then charge at the doors and bust them down. You follow with the crowd and escape prison.")
      time.sleep(3)
      victory()
  elif choice == "n":
    print("Congratulations. You missed every oppurtunity to escape.")
    time.sleep(3)
    gameover()
  
def picklock():
  global username
  print("You begin trying to pick the lock on the cell door.")
  attempt1 = int(input("Input a number between 1 and 3: "))
  while not attempt1 == 3:
    print("You fail to pick the first string.")
    caught = random.randint(1,5)
    if caught == 1:
      gameover(username)
    else:
      attempt1 = int(input("Input a number between 1 and 3: "))
    time.sleep(1)
    attempt1 = int(input("Input a number between 1 and 3: "))
  if attempt1 == 3:
    time.sleep(1)
    print("*Click*")
    attempt2 = int(input("Input a number between 1 and 3: "))
    while not attempt2 == 1:
      print("You fail to pick the first string.")
      caught = random.randint(1,5)
      if caught == 1:
        gameover(username)
      else:
        attempt2 = int(input("Input a number between 1 and 3: "))
    if attempt2 == 1:
      time.sleep(1)
      print("*Click*")
      attempt3 = int(input("Input a number between 1 and 3: "))
      while not attempt3 == 2:
        print("You fail to pick the first string.")
        caught = random.randint(1,5)
        if caught == 1:
          gameover(username)
        else:
          attempt3 = int(input("Input a number between 1 and 3: "))
      if attempt3 == 2:
        time.sleep(1)
        print("*Click*")
        time.sleep(1)
        print("\n\nYou successfully picked the lock.")
        os.system("clear")   #From https://www.scaler.com                                          /topics/how-to-clear-screen-in-python/
        escaperouts1()

def escaperouts1():
  print("OUTSIDE THE CELL\n================")
  time.sleep(1)
  print("\n\nYou enter a long hallway, a vent is on the wall right next to you. Down the end of the hall you see a T junction that goes left and right.")
  choice = input("\nWhat would you like to do?\n(a) Enter the vent\n(b) Go to the end of the hallway\n")
  while not (choice == "a" or choice == "b"):
    print("\nInvalid input.\n")
    time.sleep(1)
    choice = input("\nWhat would you like to do?\n(a) Enter the vent\n(b) Go to the end of the hallway")
  if choice == "a":
    vent()
  elif choice == "b":
    hallway()
    
def vent():
  print("You open the vent and crawl into it.")
  time.sleep(2)
  print("You crawl through the complex system of vents.")
  fall = random.randint(1,3)
  if fall == 1:
    print("You fall through a loose panel in the vent.")
    time.sleep(2)
    gameover(username)
  else:
    print("You come to a point where there are two paths you can take.")
    time.sleep(2)
    choice = input("Would you like to turn left or right?\n")
    while not (choice == "left" or choice == "right"):
      print("Invalid input.")
      time.sleep(1)
      choice = input("Would you like to turn left or right?")
    if choice == "left":
      print("You fall through a loose panel in the vent.")
      time.sleep(2)
      gameover(username)
    elif choice == "right":
      time.sleep
      print("You see daylight and open the panel in the vent.\nYou crawl out and stand on the roof of the prison. A free man once again.")
      time.sleep(5)
      victory()

  
def righthall():
  print("As you go down the hall you hear the footsteps of guards.")
  time.sleep(1)
  print("You hear footstep approaching, and dash behind a stack of boxes.")
  time.sleep(1)
  caught = random.randint(1,2)
  if caught == 1:
    print("The guard spots you hiding.")
    gameover(username)
  elif caught == 2:
    print("The guard passes by, and you continue to sneak down the hall.")
    time.sleep(1)
    print("You find a small vent at the end of the hallway.")
    choice = input("Would you like to enter the vent?\n(y/n): ")
    while not (choice == "y" or choice == "n"):
      print("\n\nInvalid input.")
      time.sleep(1)
      choice = input("Would you like to enter the vent?\n(y/n): ")
    if choice == "y":
      print("You open the vent and try to climb through, but get stuck.")
      time.sleep(1)
      gameover(username)
    elif choice == "n":
      print("You come to the end of the hallway and turn left.")
      reception()
    

def hallway():
  print("\n\nYou travel to the end of the hallway.")
  time.sleep(1)
  rorl = input("Would you like turn left, or right?\n")
  while not (rorl == "left" or rorl == "right"):
    print("\nInvalid input.")
    time.sleep(1)
    rorl = input("Would you like turn left, or right?")
  if rorl == "left":
    print("You turn left and bump into a guard.")
    fight = input("Would you like to fight him?\n(y/n):")
    while not (fight == "y" or fight == "n"):
      print("Invalid input.")
      time.sleep(1)
      fight = input("Would you like to fight him?\n(y/n):")
    if fight == "n":
      gameover(username)
    if fight == "y":
      chance = random.randint(1,2)
      if chance == 1:
        print("You are shot by the guard.")
        gameover(username)
      elif chance == 2:
        print("You KO the guard, and decide to turn around and go right.")
        righthall()
  elif rorl == "right":
    righthall()


def reception():
  print("You can see the entry of the prison.")
  time.sleep(2)
  choice = input("Should you make a dash for it, or try and be sneaky\n(dash/sneaky): ")
  while not (choice == "dash" or choice == "sneaky"):
    print("\n\nInvalid input.")
    time.sleep(1)
    choice = input("Should you make a dash for it, or try and be sneaky\n(dash/sneaky): ")
  if choice == "dash":
    dash()
  elif choice == "sneaky":
    sneaky()

def dash():
  print("You sprint for the sliding glass door to exit the prison.")
  time.sleep(1)
  print("You slam into the glass door, and knock yourself out.")
  gameover(username)

def sneaky():
  print("You tiptoe through the reception room, hiding from the guards and the workers at the desk. You crawl to the front sliding door and it opens.")
  time.sleep(1)
  print("You run out onto the road, a free man again.")
  time.sleep(3)
  os.system("clear")
  victory()

def victory():
  os.system("clear")
  print("__   _______ _   _   _    _ _____ _   _ _ \n\ \ / /  _  | | | | | |  | |_   _| \ | | |\n \ V /| | | | | | | | |  | | | | |  \| | |\n  \ / | | | | | | | | |/\| | | | | . ` | |\n  | | \ \_/ / |_| | \  /\  /_| |_| |\  |_|\n  \_/  \___/ \___/   \/  \/ \___/\_| \_(_)")