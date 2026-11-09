from game.character import Character, Team
from game.combat import Combat
from game.stand import sticky_fingers, gold_experience

class Menu:
    def run(self):
        while True:
            print("=== JoJo: Vento Aureo ===")
            print("1. Jugar")
            print("2. Salir")
            option = input("Opción: ")
            if option == "1":
                self.play()
            elif option == "2":
                print("Hasta luego")
                break
            else:
                print("Opción inválida")

    def play(self):
        p1 = Character("Bruno Bucciarati", Team.BUCCIARATI, sticky_fingers)
        p2 = Character("Giorno Giovanna", Team.BUCCIARATI, gold_experience)
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