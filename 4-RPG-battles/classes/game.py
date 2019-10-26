import random
from .magic import Spell


class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


class Person:
  def __init__(self, name, hp, mp, attack, defense, magic, items):
    self.name = name
    self.maxhp = hp
    self.hp = hp
    self.maxmp = mp
    self.mp = mp
    self.attacklo = attack - 10
    self.attackhi = attack + 10
    self.defense = defense
    self.magic = magic
    self.items = items
    self.actions = ['Attack', 'Magic', 'Item']
  
  def generate_damage(self):
    return random.randrange(self.attacklo, self.attackhi)

  def take_damage(self, damage):
    self.hp -= damage
    if self.hp < 0:
      self.hp = 0
    return self.hp

  def get_hp(self):
    return self.hp
  
  def get_max_hp(self):
    return self.maxhp
  
  def get_mp(self):
    return self.mp

  def get_max_mp(self):
    return self.maxmp

  def heal(self, hp):
    self.hp += hp

  def reduce_mp(self, cost):
    self.mp -= cost
  
  def choose_action(self):
    i = 1
    print('\n' + bcolors.BOLD + self.name + bcolors.ENDC)
    print('Actions')
    for action in self.actions:
      print(str(i) + ':', action)
      i += 1
  
  def choose_magic(self):
    i = 1
    print('Magic')
    for spell in self.magic:
      print(str(i) + ':', spell.name, '(cost:', str(spell.cost) + ')')
      i += 1

  def choose_item(self):
      i = 1
      print('Items')
      for item in self.items:
        print(str(i) + ':', item['item'].name, ':', item['item'].description, ' (x', item['quantity'],')')
        i += 1
  
  def choose_target(self, enemies):
      i = 1
      print('Enemies')
      for enemy in enemies:
        if enemy.get_hp() > 0:
          print(str(i) + ':', enemy.name)
          i += 1
      target = int(input('Choose target:')) - 1
      return target

  def reduce_item(self, i):
    self.items[i]['quantity'] -= 1

  def get_stats(self):
    name = self.name
    while len(name) < 5:
      name += ' '

    hp = str(self.hp)
    while len(hp) < 4:
      hp = ' ' + hp

    mp = str(self.mp)
    while len(mp) < 3:
      mp = ' ' + mp

    hp_bar = ''
    hp_bar_ticks = (self.hp / self.maxhp) * 100 / 4

    while hp_bar_ticks > 0:
      hp_bar += '█'
      hp_bar_ticks -= 1

    while len(hp_bar) < 25:
      hp_bar += ' '
  
    mp_bar = ''
    mp_bar_ticks = (self.mp / self.maxmp) * 100 / 10

    while mp_bar_ticks > 0:
      mp_bar += '█'
      mp_bar_ticks -= 1

    while len(mp_bar) < 10:
      mp_bar += ' '
    
    print('                      _________________________               __________')
    print(name + ':' + '     ' + hp + '/' + str(self.maxhp) + ' |' + hp_bar +  '|    ' + mp + '/' + str(self.maxmp) + '  |' + mp_bar + '|')

  def get_enemy_stats(self):
    name = self.name
    while len(name) < 5:
      name += ' '
    
    hp = str(self.hp)
    while len(hp) < 5:
      hp = ' ' + hp

    hp_bar = ''
    hp_bar_ticks = (self.hp / self.maxhp) * 100 / 2

    while hp_bar_ticks > 0:
      hp_bar += '█'
      hp_bar_ticks -= 1

    while len(hp_bar) < 50:
      hp_bar += ' '

    print('                        __________________________________________________ ')
    print(name + ':' + '     ' + hp + '/' + str(self.maxhp) + ' |' + hp_bar +  '|')
  
  def choose_enemy_spell(self):
    magic_index = random.randrange(0, 3)
    spell = self.magic[magic_index]           
    magic_damage = spell.generate_damage()
    percent = self.hp / self.maxhp * 100

    if self.mp < spell.cost or spell.type == 'white' and percent > 50:
      spell, magic_damage = self.choose_enemy_spell()
      return spell, magic_damage
    else:
      return spell, magic_damage