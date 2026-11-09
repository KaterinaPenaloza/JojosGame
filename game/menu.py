from game.character import Character, Team
from game.combat import Combat
from game.stand import sticky_fingers, gold_experience

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
        # Guardar los personajes en una lista
        characters = Character.create_characters()
        bucciarati_team = [c for c in characters if c.team == Team.BUCCIARATI]
        squadra = [c for c in characters if c.team == Team.LA_SQUADRA]

        # Elegir personaje
        print("Elija su personaje:")
        for number, c in enumerate(bucciarati_team):
            print(number, c)
        op1 = int(input("Personaje: "))
        p1 = bucciarati_team[op1]
        print(f"{p1.name} elegido \n")

        print("Elija su contrincante:")
        for number, c in enumerate(squadra):
            print(number, c)
        op2 = int(input("Enemigo: "))
        p2 = squadra[op2]
        print(f"{p2.name} elegido")

        return p1, p2

