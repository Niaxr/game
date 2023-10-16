choice = False
FALSE = 0
level = 0

class Character:
  def __init__(self, name, hp, attack, defense):
      self.name = name
      self.hp = hp
      self.attack = attack
      self.defense = defense

  def take_damage(self, damage):
      self.hp -= damage

  def is_alive(self):
      return self.hp > 0

  def attack_enemy(self, enemy):
      damage = max(0, self.attack - enemy.defense)
      enemy.take_damage(damage)
      return damage

class Enemy(Character):
  def __init__(self, name, hp, attack, defense, gold_reward):
      super().__init__(name, hp, attack, defense)
      self.gold_reward = gold_reward

  def get_gold_reward(self):
      return self.gold_reward

class Player(Character):
  def __init__(self, name):
      super().__init__(name, hp=100, attack=20, defense=10)
      self.gold = 0
      self.inventory = []

  def gain_gold(self, amount):
      self.gold += amount

  def add_to_inventory(self, item):
      self.inventory.append(item)

  def list_inventory(self):
      return self.inventory

if 

def battle(player, enemy):
  
  print(f"A wild {enemy.name} appears!\n")
  while player.is_alive() and enemy.is_alive():
      print(f"{player.name}: HP {player.hp}\t........{enemy.name}: HP {enemy.hp}\n")
      action = input("What will you do? ((A)ttack / (R)un) ").lower()
      if action == "a":
          player_damage = player.attack_enemy(enemy)
          print(f"You attack the {enemy.name} for {player_damage} damage!\n")
          if enemy.is_alive():
              enemy_damage = enemy.attack_enemy(player)
              print(f"The {enemy.name} attacks you for {enemy_damage} damage!\n")
      elif action == "r":
          print(f"You run away from the {enemy.name}!\n")
          return False
      else:
          print("Invalid action. Choose '(A)ttack' or '(R)un'.\n")


  if player.is_alive():
      gold_reward = enemy.get_gold_reward()
      player.gain_gold(gold_reward)
      print(f"You defeated the {enemy.name} and earned {gold_reward} gold!\n")
      return True
  else:
      print("You were defeated!\n")
      return False

def main():
  player_name = input("Enter your character's name: ")
  player = Player(player_name)

  while player.is_alive():
      print(f"{player.name}: HP {player.hp}\tGold: {player.gold}\n")
      choice = input("Do you want to (E)xplore, (I)nspect inventory, or (Q)uit? ").lower()

      if choice == "e":
          enemy = Enemy("Slime", hp=30, attack=10, defense=5, gold_reward=20)
          if battle(player, enemy):
              player.add_to_inventory("Slimes essence")
      elif choice == "i":
          inventory = player.list_inventory()
          if inventory:
              print("You have the following items:")
              for item in inventory:
                  print(item)
              print()
          else:
              print("Your inventory is empty.\n")
      elif choice == "q":
          print("Thanks for playing!")
          break
      else:
          print("Invalid choice. Choose 'E', 'I', or 'Q'.\n")
        
if choice == "e":
  print("You walk into the forest look for SOMETHING to enteratin you, as you continue walking your hear an odd noise, rustling of sorts")

else: print("")
        

Deal=input("Welcome to Game Hub")

#-------------START OF WHILE LOOP-------------
while choice == False:

    game=int(input("What level of difficulty would u like to play at? 1, 2 or 3?"))

    if game == 3:
        #level=int(input("This is the hardest level are you sure?"))
        choice = input("This is the hardest level... are you sure? (y / n)")

    elif game == 2:
        #print("Medium? Good choice")
        choice = input("This is the normal difficulty... are you sure? (y / n)")

    elif game == 1:
        #level=int(input("The easiest level? Are you sure?"))
        choice = input("This is the easiest level... are you sure? (y / n)")

    else:
        print("Sorry thats not possible try again")

    if choice == "y":

        print("Lets get started!")

        main()

    else:

      print("Guess u couldnt handle the heat huh :P")  

#-------------END OF WHILE LOOP-------------
