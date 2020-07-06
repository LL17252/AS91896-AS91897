class Shop():
  def __init__(self):
    self.items = ["ph scale", 'seeds']
    self.prompt = "\n\nWelcome to the shop.\n\nWhat would you like to buy?"
    self.bprompt = "\nYou have brought: \n"
    self.bitems = []
  def start(self):
    if len(self.items) != 0:
      print(self.prompt)
      for x in range(len(self.items)):
        print(str(x+1) + ". " + self.items[x])
      print("\n")

      if len(self.bitems) != 0:
        print(self.bprompt)
        for x in range(len(self.bitems)):
          print(str(x+1) + ". " + self.bitems[x])
      buy = input("> ")
      
      if len(self.items) == 2:
        if buy.lower() in (("1", "2") or self.items):
          if buy.lower() in ("1", "2"):
            buy = self.items[int(buy)-1]
          self.items.remove(buy)
          self.bitems.append(buy)
          print("You have successfully brought " + buy)
        else:
          while buy.lower() not in (("1", "2") or self.items):
            print("Please select a valid option.")
            buy = input("> ")
          if buy.lower() in ("1", "2"):
            if buy.lower() in ("1", "2"):
              buy = self.items[int(buy)-1]
          self.items.remove(buy)
          self.bitems.append(buy)
          print("You have successfully brought " + buy)
            
            
      elif len(self.items) == 1:
        if buy.lower() in (("1") or self.items):
          if buy.lower() in ("1"):
            buy = self.items[int(buy)-1]
          self.items.remove(buy)
          self.bitems.append(buy)
          print("You have successfully brought " + buy)
        else:
          while buy.lower() not in (("1") or self.items):
            print("Please select a valid option.")
            buy = input("> ")
          if buy.lower() in ("1"):
            if buy.lower() in ("1"):
              buy = self.items[int(buy)-1]
          self.items.remove(buy)
          self.bitems.append(buy)
          print("You have successfully brought " + buy)
    else:
      print("\n\nYou have brought everything! :)")
      
    
        
shop = Shop()

shop.start()
shop.start()
shop.start()
