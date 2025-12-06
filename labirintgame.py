import random
class ListLabyrinth:
    def __init__(body):
        body.inventory = []
        body.hp = 10
        body.key = False
        body.x = 0
        body.y = 0
        body.boss_x = random.randint(1, 4)
        body.boss_y = random.randint(1, 4)
        
        body.lab = []
        for i in range(5):
            row = []
            for j in range(5):
                if i == 0 and j == 0:
                    row.append("старт")
                elif i == 4 and j == 4:
                    row.append("выход")
                elif i == body.boss_y and j == body.boss_x:
                    row.append("босс")
                else:
                    row.append(random.choice(["пусто", "сундук", "монстр", "ключ", "ловушка", "портал"]))
            body.lab.append(row)
    
    def status(body):
        print(f"Жизни: {body.hp}, Ключ: {'да' if body.key else 'нет'}")
        print(f"Позиция: [{body.x},{body.y}], Инвентарь: {body.inventory}")
    
    def move(body, d):
        if d == "w" and body.y > 0:
            body.y -= 1
        elif d == "s" and body.y < 4:
            body.y += 1
        elif d == "a" and body.x > 0:
            body.x -= 1
        elif d == "d" and body.x < 4:
            body.x += 1
        else:
            print("нельзя")
            return False
        if body.x < 0 or body.x > 4 or body.y < 0 or body.y > 4:
            print("ошибка координат")
            body.x = max(0, min(4, body.x))
            body.y = max(0, min(4, body.y))
            return False
        
        room = body.lab[body.y][body.x]
        print(f"комната [{body.x},{body.y}]: {room}")
        
        if room == "выход":
            if body.key:
                print("победа!")
                return True
            else:
                print("нужен ключ")
        
        elif room == "босс":
            print("встретил монстра ты потерял хп")
            body.hp = 0
            return True
        
        elif room == "монстр":
            body.hp -= 2
            print(f"-2 жизни, осталось {body.hp}")
        
        elif room == "ловушка":
            body.hp -= 1
            print(f"-1 жизнь, осталось {body.hp}")
        
        elif room == "ключ":
            body.key = True
            print("нашел ключ!")
        
        elif room == "сундук":
            items_generator = iter(["меч", "ключ"])
            item = next(items_generator)
            print(f"нашел {item}")
            body.inventory.append(item)
        
        elif room == "портал":
            new_x = random.randint(0, 4)
            new_y = random.randint(0, 4)
            print(f"телепорт из [{body.x},{body.y}] в [{new_x},{new_y}]")
            body.x = new_x
            body.y = new_y
            if body.x < 0 or body.x > 4 or body.y < 0 or body.y > 4:
                print("ошибка телепортации")
                body.x = max(0, min(4, body.x))
                body.y = max(0, min(4, body.y))
                return False
            room_after = body.lab[body.y][body.x]
            print(f"комната после телепорта [{body.x},{body.y}]: {room_after}")
            if room_after == "выход":
                if body.key:
                    print("победа!")
                    return True
                else:
                    print("нужен ключ")
            elif room_after == "босс":
                print("встретил монстра ты потерял хп")
                body.hp = 0
                return True
            elif room_after == "монстр":
                body.hp -= 2
                print(f"-2 жизни, осталось {body.hp}")
            elif room_after == "ловушка":
                body.hp -= 1
                print(f"-1 жизнь, осталось {body.hp}")
            elif room_after == "ключ":
                body.key = True
                print("нашел ключ!")
            elif room_after == "сундук":
                items_generator = iter(["меч", "ключ"])
                item = next(items_generator)
                print(f"нашел {item}")
                body.inventory.append(item)
        
        if body.hp <= 0:
            print("проиграл")
            return True
        
        return False
    
    def commands(body, comanda):
        if comanda in ["w", "a", "s", "d"]:
            return body.move(comanda)
        
        elif comanda == "1":
            item = input("что добавить? ")
            body.inventory.append(item)
            print(f"добавил {item}")
        
        elif comanda == "2":
            items_input = input("что добавить через запятую пиши)? ")
            items = (item.strip() for item in items_input.split(",") if item.strip())
            items_list = list(items)
            body.inventory.extend(items_list)
            print(f"добавил предметы: {items_list}")
        
        elif comanda == "3":
            if body.inventory:
                item = input("что удалить? ")
                if item in body.inventory:
                    body.inventory.remove(item)
                    print(f"удалил {item}")
                else:
                    print("нет такого предмета")
            else:
                print("инвентарь пуст")
        
        elif comanda == "4":
            if body.inventory:
                item = body.inventory.pop()
                print(f"выбросил {item}")
            else:
                print("инвентарь пуст")
        
        elif comanda == "5":
            if body.inventory:
                body.inventory.sort()
                print(f"отсортировал: {body.inventory}")
            else:
                print("инвентарь пуст")
        
        elif comanda == "6":
            if body.inventory:
                body.inventory.sort(key=lambda x: len(x))
                print(f"отсортировал по длине: {body.inventory}")
            else:
                print("инвентарь пуст")
        
        elif comanda == "7":
            if body.inventory:
                item = input("позицию какого предмета найти ")
                if item in body.inventory:
                    pos = body.inventory.index(item)
                    print(f"{item} на позиции {pos}")
                else:
                    print("нет такого предмета")
            else:
                print("инвентарь пуст")
        
        elif comanda == "8":
            item = input("проверить наличие: ")
            if item in body.inventory:
                print(f"{item} есть в инвентаре")
            else:
                print(f"{item} нет в инвентаре")
        
        elif comanda == "9":
            item = input("проверить отсутствие: ")
            if item not in body.inventory:
                print(f"{item} не находится в инвентаре")
            else:
                print(f"{item} находится в инвентаре")
        
        elif comanda == "10":
            if body.inventory:
                print("предметы в инвентаре:")
                inv_iter = iter(body.inventory)
                try:
                    while True:
                        item = next(inv_iter)
                        print(f"  - {item}")
                except StopIteration:
                    pass
            else:
                print("инвентарь пуст")
        
        elif comanda == "i":
            body.status()
        
        elif comanda == "q":
            return True
        
        return False

game = ListLabyrinth()
print("найди ключ и дойди до выхода, встретив ловушку или монстра теряешь хп")
print("w  двигаться вверх")
print("s  двигаться вниз")
print("a  двигаться налево")
print("d  двигаться направо")
print("1  добавить один предмет")
print("2  добавить несколько предметов")
print("3  удалить конкретный предмет")
print("4  выбросить последний предмет")
print("5  сортировать инвентарь")
print("6  сортировать по длине названия")
print("7  найти позицию предмета")
print("8  проверить наличие предмет")
print("9  проверить притсутствие предмета")
print("10  просмотреть инвентарь (используя")
print("i  инфо об игроке")
print("q  закончить")
while True:
    comanda = input("команда: ")
    if game.commands(comanda):
        break
