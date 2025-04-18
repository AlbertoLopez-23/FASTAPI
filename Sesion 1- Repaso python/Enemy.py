class Enemy:
    def __init(self, type_of_enemy, heatlh_points, attack_damage):
        self.type_of_enemy = type_of_enemy
        self.heatlh_points = heatlh_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f'I am a {self.type_of_enemy}. be prepared to fight!')
              
    def walk_forward(self):
        print(f'{self.type_of_enemy} moves closer to you')

    def attack(self):
        print(f'{self.type_of_enemy} attacks for {self.attack_damage} damage')