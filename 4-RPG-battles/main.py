from classes.game import Person, bcolors

magic = [{'name': 'Fire', 'cost': 10, 'damage': 100},
         {'name': 'Thunder', 'cost': 10, 'damage': 124},
         {'name': 'Blizzard', 'cost': 10, 'damage': 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 24, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!' + bcolors.ENDC)  #end the style with ENDC

while running:
  print('==================================')
  player.choose_action()
  action_choice = input('Choose action:')
  action_index = int(action_choice) - 1   #index starts with 0
  
  if action_index == 0:
    damage = player.generate_damage()
    enemy.take_damage(damage)
    print('You attacked for', str(damage), 'points of damage')
  elif action_index == 1:
    player.choose_magic()
    magic_index = int(input('Choose magic:')) - 1
    spell = player.get_spell_name(magic_index)
    cost = player.get_spell_cost(magic_index)
    magic_damage = player.generate_spell_damage(magic_index)
    current_mp = player.get_mp()

    if current_mp < cost:
      print(bcolors.FAIL + '\nYou dont have enough mp\n' + bcolors.ENDC)
      continue

    player.reduce_mp(cost)
    enemy.take_damage(magic_damage)
    print(bcolors.OKBLUE + '\n' + spell + 'deals', str(magic_damage), 'points of damage' + bcolors.ENDC)

  enemy_choice = 1
  enemy_damage = enemy.generate_damage()
  player.take_damage(enemy_damage)
  print('Enemy attacked for', enemy_damage, 'points of damage')

  print('========================================')
  print('Enemy HP:', bcolors.FAIL + str(enemy.get_hp()) + '/' + str(enemy.get_max_hp()) + bcolors.ENDC)

  print('Your HP:', bcolors.OKGREEN + str(player.get_hp()) + '/' + str(player.get_max_hp()) + bcolors.ENDC)
  print('Your MP:', bcolors.OKBLUE + str(player.get_mp()) + '/' + str(player.get_max_mp()) + bcolors.ENDC)

  if enemy.get_hp() == 0:
    print(bcolors.OKGREEN + 'You win!' + bcolors.ENDC)
    running = False
  elif player.get_hp() == 0:
    print(bcolors.FAIL + 'You have been defeated by the enemy!' + bcolors.ENDC)
    running = False
