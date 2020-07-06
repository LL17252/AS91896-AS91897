class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 20
        self.mp = 20
        self.inventory = []
        self.location = "a1"
        self.game_over = False
myPlayer = player()


class Shop():
  def __init__(self, items = []):
    self.items = items
    self.prompt = "\n\nWelcome to the shop.\n\nWhat would you like to buy?"
    self.bprompt = "You have brought: "
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
        print('\n')
      buy = input("> ")
      
      if len(self.items) != 0:
        list = []
        for x in range(len(self.items)):
          list.append(str(x+1))
        if buy.lower() in (list or self.items):
          if buy.lower() in list:
            buy = self.items[int(buy)-1]
          self.items.remove(buy)
          self.bitems.append(buy)
          myPlayer.inventory.append(buy)
          print("You have successfully brought " + buy)
        else:
          while buy.lower() not in (list or self.items):
            print("Please select a valid option.")
            buy = input("> ")
          if buy.lower() in list:
            buy = self.items[int(buy)-1]
          self.items.remove(buy)
          self.bitems.append(buy)
          myPlayer.inventory.append(buy)
          print("You have successfully brought " + buy)
            
    else:
      print("\n\nYou have brought everything! :)")
      
    
        
shop = Shop(["ph scale", "seeds"])

shop.start()
print(myPlayer.inventory)
shop.start()
shop.start()
print(myPlayer.inventory)




