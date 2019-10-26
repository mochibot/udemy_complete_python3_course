from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

#creating black magic
fire = Spell('Fire', 25, 500, 'black')
thunder = Spell('Thunder', 25, 600, 'black')
blizzard = Spell('Blizzard', 25, 800, 'black')
meteor = Spell('Meteor', 40, 1200, 'black')
quake = Spell('Quake', 14, 140, 'black')


#creating white magic
cure = Spell('Cure', 25, 620, 'white')
cura = Spell('Cura', 32, 1500, 'white')
curaga = Spell('Curaga', 50, 6000, 'white')

# create some items
potion = Item('Potion', 'potion', 'heals 50 HP', 50)
hipotion = Item('Hi-potion', 'potion', 'heals 100 HP', 100)
superpotion = Item('Super-potion', 'potion', 'heals 500 HP', 1000)
elixir = Item('Elixir', 'elixir', 'Full restores HP/MP of 1 party member', 9999)
megaelixir = Item('MegaElixir', 'elixir', 'Full restores party\'s HP/MP', 9999)
grenade = Item('Grenade', 'attack', 'Deals 500 damage', 500)

player_spell = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{'item': potion, 'quantity': 15}, {'item': hipotion, 'quantity': 5},
                {'item': superpotion, 'quantity': 5}, {'item': elixir, 'quantity': 5},
                {'item': megaelixir, 'quantity': 2}, {'item': grenade, 'quantity': 5}]

enemy1_spell = [fire, meteor, curaga]
enemy_spell = [fire, meteor, cure]
  
# instantiate players
player1 = Person('Valos', 3260, 132, 300, 34, player_spell, player_items)
player2 = Person('Blah', 4160, 188, 338, 34, player_spell, player_items)
player3 = Person('Test', 3089, 174, 299, 34, player_spell, player_items)
enemy1 = Person('Boss', 18200, 701, 525, 24, enemy1_spell, [])
enemy2 = Person('Imp1', 1250, 130, 560, 325, enemy_spell, [])
enemy3 = Person('Imp2', 1250, 130, 560, 325, enemy_spell, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!' + bcolors.ENDC)  #end the style with ENDC

while running:
  print('==================================')
  print('NAME                  HP                                      MP')
  
  for player in players:  
    player.get_stats();
    print('\n')

  for enemy in enemies:
    enemy.get_enemy_stats();
    print('\n')

  #players attack phase
  for player in players:
    player.choose_action()
    action_choice = input('Choose action:')
    action_index = int(action_choice) - 1          #index starts with 0
    
    if action_index == 0:
      enemy = player.choose_target(enemies)
      damage = player.generate_damage()
      enemies[enemy].take_damage(damage)
      print(player.name, 'attacked', enemies[enemy].name, 'for', str(damage), 'points of damage')

      if enemies[enemy].get_hp() == 0:
        print(enemies[enemy].name, 'has died')
        del enemies[enemy]    

    elif action_index == 1:
      player.choose_magic()
      magic_index = int(input('Choose magic:')) - 1

      if magic_index == -1:                       #can hit 0 to get back
        continue

      spell = player.magic[magic_index]           #spell will be an object from the array
      magic_damage = spell.generate_damage()

      current_mp = player.get_mp()

      if current_mp < spell.cost:
        print(bcolors.FAIL + 'Not have enough mp' + bcolors.ENDC)
        continue

      player.reduce_mp(spell.cost)

      if spell.type == 'white':
        player.heal(magic_damage)
        print (bcolors.OKBLUE + spell.name, 'heals', player.name, 'for', str(spell.type), 'HP' + bcolors.ENDC)
      elif spell.type == 'black':
        enemy = player.choose_target(enemies)
        enemies[enemy].take_damage(magic_damage)
        print(bcolors.FAIL + spell.name, 'deals', str(magic_damage), 'points of damage to', enemies[enemy].name + bcolors.ENDC)

        if enemies[enemy].get_hp() == 0:
          print(enemies[enemy].name, 'has died')
          del enemies[enemy]   
    
    elif action_index == 2:
      player.choose_item()
      item_index = int(input('Choose item:')) - 1

      if item_index == -1:                        #can hit 0 to get back
        continue

      if player.items[item_index]['quantity'] == 0:
        print(bcolors.FAIL + 'No more', player.items[item_index]['item'].name, 'left' + bcolors.ENDC)
        continue
      
      item = player.items[item_index]['item']              #item will be an object from the array
      player.reduce_item(item_index)

      if item.type == 'potion':
        player.heal(item.prop)
        print (bcolors.OKBLUE + item.name, 'heals for', str(item.prop), 'HP' + bcolors.ENDC)
      elif item.type == 'elixir':
        if item.name == 'MegaElixir':
          for person in players:
            person.hp = person.maxhp
            person.mp = person.maxmp
            print (bcolors.OKGREEN + player.name, 'fully restored to', str(player.get_hp()), 'HP', '/', str(player.get_mp()), 'MP' + bcolors.ENDC)
        else: 
          player.hp = player.maxhp
          player.mp = player.maxmp
          print (bcolors.OKGREEN + player.name, 'fully restored to', str(player.get_hp()), 'HP', '/', str(player.get_mp()), 'MP' + bcolors.ENDC)
      elif item.type == 'attack':
        enemy = player.choose_target(enemies)
        enemies[enemy].take_damage(item.prop)
        print (bcolors.FAIL + item.name, 'deals', str(item.prop), 'points of damage to', enemies[enemy].name + bcolors.ENDC)

        if enemies[enemy].get_hp() == 0:
          print(enemies[enemy].name, 'has died')
          del enemies[enemy]  

  #check if battle is over
  defeated_enemies = 0
  defeated_players = 0

  for enemy in enemies:
    if enemy.get_hp() == 0:
      defeated_enemies += 1
  
  for player in players:
    if player.get_hp() == 0:
      defeated_players += 1

  if defeated_enemies == len(enemies):
    print(bcolors.OKGREEN + 'You win!' + bcolors.ENDC)
    running = False
  elif defeated_players == len(players):
    print(bcolors.FAIL + 'You have been defeated by the enemies!' + bcolors.ENDC)
    running = False

  print('\n')
  #enemies attack phase
  for enemy in enemies:
    enemy_choice = random.randrange(0, 2)

    if enemy_choice == 0:
      target = random.randrange(0, len(players))
      enemy_damage = enemy.generate_damage()
      players[target].take_damage(enemy_damage)
      print(enemy.name, 'attacked', players[target].name, 'for', enemy_damage, 'points of damage')

    elif enemy_choice == 1:
      spell, magic_damage = enemy.choose_enemy_spell()
      enemy.reduce_mp(spell.cost)

      if spell.type == 'white':
        enemy.heal(magic_damage)
        print (bcolors.OKBLUE + spell.name, 'heals', enemy.name,'for', str(spell.type), 'HP' + bcolors.ENDC)
      elif spell.type == 'black':
        target = random.randrange(0, len(players))
        players[target].take_damage(magic_damage)
        print(bcolors.FAIL + enemy.name, ':', spell.name, 'deals', str(magic_damage), 'points of damage to', players[target].name + bcolors.ENDC)

        if players[target].get_hp() == 0:
          print(players[target].name, 'has died')
          del players[target]  

    