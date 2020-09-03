import os
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
  def __init__(self, items = [],itemdesu = []):
    self.items = items
    self.itemdesu = itemdesu
    self.prompt = "\n\nWelcome to the shop.\n\nWhat would you like to buy?"
    self.bprompt = "You have brought: "
    self.bitems = []
#to start the shop
  def start(self):
    if len(self.items) != 0:
      print(self.prompt)
      for x in range(len(self.items)):
        print(str(x+1) + ". " + self.items[x])
      print("\n")

      if len(self.bitems) != 0:#if items have been brought then it will print what items have been brought
        print(self.bprompt)
        for x in range(len(self.bitems)):
          print(str(x+1) + ". " + self.bitems[x])
        print('\n')

      
      if len(self.items) != 0:#if there are still items left it will open the shop and allow for purchase. You can purchase by using the number given or by the item name
        num = []
        for x in range(len(self.items)):
          num.append(str(x+1))
        buy = input("> ")
        if buy.lower() in (num):
          os.system('clear')
          description = self.itemdesu[int(buy)-1]
          self.itemdesu.pop(int(buy)-1)
          buy = self.items[int(buy)-1]
          self.items.remove(buy)
          self.bitems.append(buy)
          myPlayer.inventory.append(buy)
          print("You have successfully bought " + buy)
          print(description)
        else:
          while buy.lower() not in (num):
            print("Please select a valid option.(Number of the item only)")
            buy = input("> ")
          os.system('clear')
          description = self.itemdesu[int(buy)-1]
          self.itemdesu.pop(int(buy)-1)
          buy = self.items[int(buy)-1]
          self.items.remove(buy)
          self.bitems.append(buy)
          myPlayer.inventory.append(buy)
          print("You have successfully bought " + buy)
          print(description)

    else:
      print("\n\nYou have brought everything! :)")
