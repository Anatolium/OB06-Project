class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"У игрока {self.name} осталось здоровья: {self.health}"


class Game:
    def __init__(self, name):
        self.player = Hero(name)
        self.computer = Hero("Компьютер")

    def start(self):
        print(f"Игра началась! Игрок {self.player.name} против {self.computer.name}\n")
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            attacker, defender = (self.player, self.computer) if turn % 2 == 0 else (self.computer, self.player)
            attacker.attack(defender)
            print(f"---> {attacker.name} атаковал {defender.name}.")
            print(f"{defender}\n")
            if not defender.is_alive():
                print(f"***** {defender.name} побеждён! Победитель – {attacker.name}! *****")
                break
            turn += 1


player_name = input("Введите имя игрока: ")
game = Game(player_name)
game.start()
