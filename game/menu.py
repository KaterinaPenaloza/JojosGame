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
    def choose_from(options, equipo):
        print(f"Elija {equipo}:")
        print(0, "random")
        for number, c in enumerate(options, start=1):
            print(number, c)

        while True:
            text = input("Opción: ").strip()
            if text.isdecimal() and int(text) <= len(options):
                break
            print("Opción inválida, intente de nuevo.")

        number = int(text)
        chosen = random.choice(options) if number == 0 else options[number - 1]
        print(f"{chosen.name} elegido\n")
        return chosen

    @staticmethod
    def choose_characters():
        characters = Character.create_characters()
        bucciarati_team = [c for c in characters if c.team == Team.BUCCIARATI]
        squadra = [c for c in characters if c.team == Team.LA_SQUADRA]

        p1 = Menu.choose_from(bucciarati_team, "su personaje")
        p2 = Menu.choose_from(squadra, "su contrincante")
        return p1, p2