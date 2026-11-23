from enum import Enum
from random import randint
from game.stand import *
from dataclasses import dataclass


class Team(Enum):
    BUCCIARATI = "Team Bucciarati"
    LA_SQUADRA = "La Squadra Esecuzioni"

@dataclass
class AttackResult:
    base_damage: int
    imprecise: bool
    damage_after_precision: int
    reacted: bool
    damage_after_reaction: int
    final_damage: int

class Character:
    def __init__(self, name, team, stand):
        self.name = name
        self.team = team
        self.stand = stand
        self.max_life = 100
        self._life = self.max_life

    def __str__(self):
        return f"{self.name} ({self.stand})"

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
        base_damage = round((self.stand.power + randint(0, 5))*2 * (0.5 + 0.5 * life_prop))
        return base_damage

    def attack(self, rival):
        base_damage = self.damage()
        imprecise = self.is_imprecise()
        after_precision = round(base_damage * 0.8) if imprecise else base_damage
        reacted = rival.defends()
        after_reaction = round(after_precision * 0.7) if reacted else after_precision
        final_damage = max(1, after_reaction - rival.stand.durability)
        rival.take_damage(final_damage)
        return AttackResult(base_damage, imprecise, after_precision,
                            reacted, after_reaction, final_damage)

    def defends(self):
        chance = self.stand.speed * 10
        return randint(1, 100) <= chance

    def is_imprecise(self):
        chance = (5 - self.stand.precision) * 10
        return randint(1, 100) <= chance

    @classmethod
    def create_characters(cls):
        return [
            Character("Bruno Bucciarati", Team.BUCCIARATI, sticky_fingers),
            Character("Giorno Giovanna", Team.BUCCIARATI, gold_experience),
            Character("Guido Mista", Team.BUCCIARATI, sex_pistols),
            Character("Narancia Ghirga", Team.BUCCIARATI, aerosmith),
            Character("Pannacotta Fugo", Team.BUCCIARATI, purple_haze),
            Character("Leone Abbacchio", Team.BUCCIARATI, moody_blues),
            Character("Trish Una", Team.BUCCIARATI, spice_girl),
            Character("Risotto Nero", Team.LA_SQUADRA, metallica),
            Character("Formaggio", Team.LA_SQUADRA, little_feet),
            Character("Illuso", Team.LA_SQUADRA, man_in_the_mirror),
            Character("Prosciutto", Team.LA_SQUADRA, grateful_death),
            Character("Pesci", Team.LA_SQUADRA, beach_boy),
            Character("Melone", Team.LA_SQUADRA, baby_face),
            Character("Ghiaccio", Team.LA_SQUADRA, white_album),
        ]