# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:42:59 2022

@author: Guilherme
"""

class Creature():
    def __init__(self, hp, mp):
        self.hp = hp
        self.mp = mp
        self.hp_max = hp
        self.mp_max = mp
        
    def print_status(self):
        print(f"Life: {self.hp:^4}\n"
              f"Mana: {self.mp:^4}")
        
    def lose_hp(self, hp_lost):
        self.hp -= hp_lost
    
    def lose_mp(self, mp_lost):
        self.mp -= mp_lost

class Hero(Creature):
    def __init__(self, hp, mp):
        super().__init__(hp, mp)
    
    def status(self):
        print("Player")
        super().print_status()
        print()
    
    def attack(self, target):
        hit = 5
        print(f"Hero attack | {hit} of damage\n")
        target.lose_hp(hit)
        
class Enemy(Creature):
    def __init__(self, hp, mp):
        super().__init__(hp, mp)
        
    def status(self):
        print("Enemy")
        super().print_status()
        print()
        
    def attack(self, target):
        hit = 3
        print(f"Enemy attack | {hit} of damage\n")
        target.lose_hp(hit)


def main():
    
    warrior = Hero(100, 20)
    wolf = Enemy(40, 10)
    
    warrior.status()
    wolf.status()
    
    warrior.attack(wolf)
    wolf.attack(warrior)
    warrior.attack(wolf)
    wolf.attack(warrior)
    
    warrior.status()
    wolf.status()
    
    
if __name__ == '__main__':
    main()
