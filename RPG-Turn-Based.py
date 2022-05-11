# -*- coding: utf-8 -*-

"""
@author: Guilherme
"""

class Creature():
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.hp_max = hp
        self.mp_max = mp
    
    def __str__(self):
        return f"Creature: {self.name}"
    
    def status(self):
        print(f"{self.name}\n"
              f"Life: {self.hp:^4}\n"
              f"Mana: {self.mp:^4}\n")
        
    def lose_hp(self, hp_lost):
        if self.hp > hp_lost:
            self.hp -= hp_lost
        else:
            self.hp = 0
    
    def lose_mp(self, mp_lost):
        if self.mp > mp_lost:    
            self.mp -= mp_lost
        else:
            self.mp = 0
    
    def is_alive(self):
        return self.hp > 0
    
class Hero(Creature):
    def __init__(self, name, hp, mp):
        super().__init__(name, hp, mp)
        
    def action(self, target):
        
        act = input("""What you gonna do?
        A - Attack | H - Potion | S - Status of Battle | P - pass turn
        """)
        if act in "aA":
            self.attack(target=target)
        elif act in "hH":
            self.__use_potion()
        elif act in "sS":
            self.status()
            target.status()
        elif act in "pP":
            print("You've pass your turn")
        else:
            pass
        
    def attack(self, target):
        hit = 6
        print(f"{self.name} attack | {hit} of damage\n")
        target.lose_hp(hit)
    
    def __use_potion(self):
        cure = 2
        self.hp += cure 
        print(f"{self.name} heal | {cure} of hp\n")
        
class Enemy(Creature):
    def __init__(self, name, hp, mp):
        super().__init__(name, hp, mp)
        
    def attack(self, target):
        hit = 3
        print(f"{self.name} attack | {hit} of damage\n")
        target.lose_hp(hit)


def main():
    
    warrior = Hero("Warrior", 100, 20)
    wolf = Enemy("Wolf", 40, 10)

    while warrior.is_alive() and wolf.is_alive():
        warrior.action(wolf)
        wolf.attack(warrior)
    
    warrior.status()
    wolf.status()
    print("Player Wins!") if warrior.is_alive() else print("Player Losed!")
    
    
if __name__ == '__main__':
    main()
