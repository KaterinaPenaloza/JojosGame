import random

from game.character import Character, Team
from game.combat import Combat

class Menu:
    def run(self):
        while True:
            print("=== JoJo's Bizarre Adventure: Vento Aureo ===")
            print("1. Empezar nueva partida")
            print("2. Salir")
            option = input("Opción: \n")
            match option:
                case "1":
                    self.play()
                case "2":
                    print("Hasta luego")
                    break
                case _:
                    print("Opción inválida")

    def play(self):
        p1, p2 = self.choose_characters()
        combat = Combat(p1, p2)

        while not combat.game_over():
            print(f"\n{p1.name}: {p1.life} | {p2.name}: {p2.life}")
            print(f"Turno de {combat.attacker.name}")
            print("1. Atacar")
            print("2. Rendirse")
            action = input("Acción: ")
            if action == "1":
                attacker, defender, damage = combat.execute_turn()
                print(f"{attacker} ataca a {defender} y le hace {damage} de daño")
            elif action == "2":
                combat.surrender()
            else:
                print("Acción inválida")

        print(f"\nGanó {combat.winner()}")

    @staticmethod
    def choose_characters():
        characters = Character.create_characters()
        bucciarati_team = [c for c in characters if c.team == Team.BUCCIARATI]
        squadra = [c for c in characters if c.team == Team.LA_SQUADRA]

        # Elegir personaje
        print("Elija su personaje:")
        print(0, "random")
        for number, c in enumerate(bucciarati_team, start=1):
            print(number, c)

        try:
            op1 = int(input("Personaje: "))
            p1 = random.choice(bucciarati_team) if op1 == 0 else bucciarati_team[op1 - 1]
        except (ValueError, IndexError):
            print("Entrada inválida, asignando personaje aleatorio por defecto.")
            p1 = random.choice(bucciarati_team)

        print(f"{p1.name} elegido \n")

        # Elegir contrincante
        print("Elija su contrincante:")
        print(0, "random")
        for number, c in enumerate(squadra, start=1):
            print(number, c)

        try:
            op2 = int(input("Enemigo: "))
            p2 = random.choice(squadra) if op2 == 0 else squadra[op2 - 1]
        except (ValueError, IndexError):
            print("Entrada inválida, asignando contrincante aleatorio por defecto.")
            p2 = random.choice(squadra)

        print(f"{p2.name} elegido")

        return p1, p2