from enum import Enum
from random import randint
from game.stand import sticky_fingers, gold_experience, sex_pistols, aerosmith, purple_haze, moody_blues, spice_girl

class Team(Enum):
    BUCCIARATI = "Team Bucciarati"
    LA_SQUADRA = "La Squadra Esecuzioni"

class Character:
    def __init__(self, name, team, stand):
        self.name = name
        self.team = team
        self.stand = stand
        self.max_life = 100
        self._life = self.max_life

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, value):
        if value < 0:
            self._life = 0
        elif value > self.max_life:
            self._life = self.max_life
        else:
            self._life = value

    def take_damage(self, damage):
        if self.is_alive():
            self.life -= damage

    def heal(self, amount):
        if self.is_alive() and amount > 0:
            self.life += amount

    def is_alive(self):
        return self.life > 0

    def damage(self):
        """ Daño hecho por el personaje: es proporcional del poder del stand + un random entre 0 y 3
        y multiplicado por la proporcion de la vida que le quede
        mientras más debil menos daño hace, pero sin bajar de la mitad del daño que tiene"""
        life_prop = self.life / self.max_life
        base_damage = round((self.stand.power + randint(0, 3)) * (0.5 + 0.5 * life_prop))
        return base_damage

    def attack(self, rival):
        damage = self.damage()
        damage -= rival.stand.durability
        if damage < 1:
            damage = 1
        rival.take_damage(damage)
        return damage

# Team Bucciarati
bucciarati = Character("Bruno Bucciarati", Team.BUCCIARATI, sticky_fingers)
giorno = Character("Giorno Giovanna", Team.BUCCIARATI, gold_experience)
mista = Character("Guido Mista", Team.BUCCIARATI, sex_pistols)
narancia = Character("Narancia Ghirga", Team.BUCCIARATI, aerosmith)
fugo = Character("Pannacotta Fugo", Team.BUCCIARATI, purple_haze)
abbacchio = Character("Leone Abbacchio", Team.BUCCIARATI, moody_blues)
trish = Character("Trish Una", Team.BUCCIARATI, spice_girl)
