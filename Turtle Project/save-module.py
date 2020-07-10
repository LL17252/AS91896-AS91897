import pickle


def save():
  f = open('savefile.dat', 'wb')
  pickle.dump(myPlayer, f, protocol = 2)
  f.close


def load():
  global myPlayer
  f = open('savefile.dat', 'rb')
  myPlayer = pickle.load(f)
  f.close

def saveprompt():
  print("do you wish to save?\n")
  s = input("> ")
  while s.lower() not in ("yes", 'no'):
    print("please select a valid option for saving")
    print("(yes or no)")
  if s.lower() == "yes":
    print("Now saving...")
    save()
  elif s.lower() == "no":
    print("you have chosen not to save")

def loadprompt():
  print("Do you wish to load? ")
  s = input("> ")
  while s.lower() not in ("yes", 'no'):
    print("please select a valid option for loading")
    print("(yes or no)")
  if s.lower() == "yes":
    print("Now loading...")
    load()
  elif s.lower() == "no":
    print("you have chosen not to load")
