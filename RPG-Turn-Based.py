# -*- coding: utf-8 -*-
"""
@author: Guilherme Iram
"""
import os
import time
import random

#collors
RED   = "\033[1;31m"
YELLOW = "\033[1;33m" 
BLUE  = "\033[1;34m"
GREEN = "\033[0;32m"

RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

class Creature():
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.hp_max = hp
        self.mp_max = mp
        self.atk_max = None
        self.atk_min = None

    def __str__(self):
        return f"Creature: {self.name}"

    def status(self):
        
        char_status = self.name;
        
        n_of_hearts = int((self.hp / self.hp_max) * 10)
        n_of_mana_bar = int((self.mp / self.mp_max) * 10)
        
        if n_of_hearts >= 7:
            color = GREEN
        elif n_of_hearts >= 4:
            color = YELLOW
        else:
            color = RED
            
        life = "\nLife: "
        for i in range(n_of_hearts):
            life = life + color + "O" 
        
        if n_of_hearts == 0 and self.is_alive():
            life = life + color + "O"
            n_of_hearts = 1
        
        emphy_spaces = 10 - n_of_hearts
        life += " " * emphy_spaces
        life += f" {self.hp}/{self.hp_max}" + RESET + "\n"
        char_status += life
        mana = f"Mana: " + BLUE + "O" * n_of_mana_bar + f" {self.mp}/{self.mp_max}" + RESET + "\n"
        char_status += mana
        
        print(char_status)

    def lose_hp(self, hp):
        if self.hp > hp:
            self.hp -= hp
        else:
            self.hp = 0

    def lose_mp(self, mp):
        if self.mp > mp:
            self.mp -= mp
        else:
            self.mp = 0

    def gain_hp(self, hp):
        if self.hp > hp:
            self.hp += hp
        else:
            self.hp = self.hp_max

    def gain_mp(self, mp):
        if self.mp > mp:
            self.mp += mp
        else:
            self.mp = self.mp_max

    def is_alive(self):
        return self.hp > 0


class Hero(Creature):
    def __init__(self, name, hp, mp):
        super().__init__(name, hp, mp)
        self.atk_max = 8
        self.atk_min = 0
        self.potion = 5

    def action(self, target):

        act = input("""What you gonna do?
        \n\tA - Basic Attack\n\tH - Potion\n\tS - Status of Battle\n\tP - pass turn\n\nYour move: """)
        
        os.system('cls||clear')
        
        if act in "aA":
            self.attack(target=target)
            
        elif act in "hH":
            if self.potion > 0:
                self.__use_potion()
                
            else:
                print("Out of potion!\n")
                self.action(target)
            
        elif act in "sS":
            self.status()
            target.status()
            self.action(target)
            
        elif act in "pP":
            print("You've pass your turn\n")
            
        else:
            pass
        

    def attack(self, target):
        
        hit = random.randint(self.atk_min, self.atk_max)
        critic = random.randint(0, 100)
        min_critic = 75
        critic_attack = critic >= min_critic
        
        if (hit > 0):
            if (critic_attack):
                print(f"CRITIC! {self.name} attack | {hit * 2} of damage\n")
                target.lose_hp(hit * 2)
            else:
                print(f"{self.name} attack | {hit} of damage\n")
                target.lose_hp(hit)
        else:
            print(f"{self.name} miss the attack!\n")
        
    def __use_potion(self):
        cure = 5
        if self.hp + cure >= self.hp_max:
            pass
        else:
            self.hp += cure
            self.potion -= 1
        print(f"You use 1 of yours {self.potion} potions!\n")
        print(f"{self.name} heal | {cure} of hp\n")


class Enemy(Creature):
    def __init__(self, name, hp, mp):
        super().__init__(name, hp, mp)
        self.atk_max = 12
        self.atk_min = 4

    def attack(self, target):
        
        hit = random.randint(self.atk_min, self.atk_max)
        critic = random.randint(0, 100)
        min_critic = 50
        critic_attack = critic >= min_critic
        
        if (hit > 0):
            if (critic_attack):
                print(f"CRITIC! {self.name} attack | {hit * 2} of damage\n")
                target.lose_hp(hit * 2)
            else:
                print(f"{self.name} attack | {hit} of damage\n")
                target.lose_hp(hit)
        else:
            print(f"{self.name} miss the attack!\n")


def print_start():
    print("RPG - FINAL BATTLE FANTASY\n")

def main():

    warrior = Hero("Warrior", 100, 20)
    wolf = Enemy("Wolf", 40, 10)
    
    print_start()
    
    while warrior.is_alive() and wolf.is_alive():
        
        warrior.action(wolf)
        wolf.attack(warrior)
        time.sleep(0.5)
        warrior.status()
        wolf.status()
        

    if warrior.is_alive():
        print("PLAYER WINS!")
    elif wolf.is_alive():
        print("PLAYER LOSE!")
    else:
        print("DRAW")
        
if __name__ == '__main__':
    main()
