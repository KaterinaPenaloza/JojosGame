from game.character import Character


class Combat:
    def __init__(self, j1: Character, j2: Character):
        if j1.stand.speed >= j2.stand.speed:
            self.attacker = j1
            self.defender = j2
        else:
            self.attacker = j2
            self.defender = j1
        self.surrendered = None

    def execute_turn(self):
        attacker, defender = self.attacker.name, self.defender.name
        damage = self.attacker.attack(self.defender)
        self.attacker, self.defender = self.defender, self.attacker
        return attacker, defender, damage

    def surrender(self):
        self.surrendered = self.attacker

    def winner(self):
        if self.surrendered is not None:
            winner = self.defender.name
        elif self.attacker.life == 0:
            winner = self.defender.name
        elif self.defender.life == 0:
            winner = self.attacker.name
        else:
            return None
        return winner

    def game_over(self):
        return self.winner() is not None