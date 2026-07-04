import json
import os
import random
import time
from npc import Player, Sans

class Game:
    def init(self):
        self.player = Player()
        self.sans = Sans()
        self.save_file = "sans_corridor_save.json"

    def save_game(self):
        f = open(self.save_file, "w", encoding="utf-8")
        json.dump(self.player.to_dict(), f, ensure_ascii=False, indent=4)
        f.close()
        print("\n игра сохранена кароч")

    def load_game(self):
        if os.path.exists(self.save_file):
            f = open(self.save_file, "r", encoding="utf-8")
            data = json.load(f)
            f.close()
            self.player.load_dict(data)
            print("\n загрузились! здарова опять " + self.player.name)
            return True
        return False

    def start_sans_battle(self):
        print("\n ты подошел и " + self.sans.talk())
        
        while self.sans.hp > 0 and self.player.hp > 0:
            self.player.show_stats()
            choice = input("1. АТАКА | 2. ДЕЙСТВИЕ | 3. ВЕЩИ | 4. ПОЩАДА\nче делать: ")

            if choice == "1":
                if self.sans.dodges_left > 0:
                    print("\n ты машеш ножом но санс увернулся")
                    self.sans.dodges_left = self.sans.dodges_left - 1
                else:
                    self.sans.hp = 0
                    print("\n ПОПАЛ!!! НА САНС УДАР НА 9999999 УРОНА!!! УРА ВЫЙГРАЛ!")
                    break

            elif choice == "2":
                print("\n санс короче атк " + str(self.sans.attack) + " зщт 1 самый изи враг")

            elif choice == "3":
                if self.player.inventory:
                    print("\nче сожрать:")
                    i = 1
                    for item in self.player.inventory:
                        print(str(i) + ". " + item)
                        i = i + 1
                    food_choice = input("номер еды: ")
                    if food_choice != "0" and food_choice != "":
                        item_idx = int(food_choice) - 1
                        if 0 <= item_idx < len(self.player.inventory):
                            chosen_item = self.player.inventory.pop(item_idx)
                            if chosen_item == "кусок пирага":
                                self.player.heal(20, chosen_item)
                            else:
                                self.player.heal(12, chosen_item)
                else:
                    print("\n еда кончилась капец!")

            elif choice == "4":
                if self.sans.dodges_left <= 2:
                    print("санс говорит: ладно давай мирится иди обнимемся")
                    if input("1. обнять | 2. дратся: ") == "1":
                        print("\n санс заспавнил сто костей в твое сердечко")
                        self.player.hp = 0
                        print(" ГЕЙМОВЕР!!!")
                        break
                else:
                    print("санс говорит: какая пощада ты всех убил")

            if self.sans.hp > 0 and self.player.hp > 0:
                print("\n" + self.sans.get_attack_phrase())
                time.sleep(1)
                if random.random() < 0.40:
                    print(" ТЫ УВЕРНУЛСЯ КАК НИНДЗЯ!!!")
                else:
                    self.player.hp = self.player.hp - self.sans.attack
                    print(" БАБАХ! ты получил " + str(self.sans.attack) + " урона!")
                    
                if self.player.hp <= 0:
                    print("\n твое сердечко сломалось... НЕ СДАВАЙСЯ ДАВАЙ...")

    def run(self):
        print("=== АНДЕРТЕЙЛ КОРИДОР САНСА ===")
        if input("1. заново | 2. загрузить сохранку: ") == "2" and self.load_game():
            pass
        else:
            self.player.name = input("как зовут челика: ")

        if input("1. сохранится у звезды | 2. сразу дратся: ") == "1":
            self.save_game()
        
        self.start_sans_battle()

if name == "main":
    game = Game()
    game.run()