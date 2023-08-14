cmd = ""
value = ""

pets = dict()

def create():
    name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца питомца: ")

    last_key = 1

    if pets:
        last_key = list(pets.keys())[-1]
    
    if last_key not in pets:
        pets[last_key] = {}

    pets[last_key][name] = {
        "Вид питомца": pet_type,
        "Возраст": age,
        "Имя владельца": owner_name
    }
    print("Питомец занесен в словарь.")

def read():
    if 1 not in pets:
        return print("В словаре нет питомцев.")
    name = str(list(pets[1].keys())[0])

    print("Это", pets[1][name]["Вид питомца"], "по кличке", name + ".", "Возраст питомца:", get_suffix(pets[1][name]["Возраст"]) + ".", "Имя владельца:", pets[1][name]["Имя владельца"])

def update(n):
    if n not in pets:
        return print("Записи с данным ID не существует.")
    
    del pets[n]
    pets[n] = {}

    name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца питомца: ")

    pets[n][name] = {
        "Вид питомца": pet_type,
        "Возраст": age,
        "Имя владельца": owner_name
    }
    print("Питомец занесен в словарь.")

def delete(n):
    if n not in pets:
        return print("Записи с данным ID не существует.")
    if n == 1:
        del pets
        print("Словарь удален.")
    else:
        del pets[n]
        print("Запись удалена.")

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return f"{age} год"
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        return f"{age} года"
    else:
        return f"{age} лет"

def pets_list():
    if not pets:
        return print("Нет записей в словаре.")
    for i in pets.keys():
        print(pets[i])
    

while True:
    user_input = input()
    
    part = user_input.split(" ")

    cmd, val = "", None

    if len(part) >= 2:
        cmd = part[0]
        try:
            val = int(part[1])
        except ValueError:
            print("Некорректная команда.")
    else:
        cmd = user_input

    if cmd == "create":
        create()
    elif cmd == "read" and val is not None:
        read(int(val))
    elif cmd == "update" and val is not None:
      update(int(val))
    elif cmd == "delete" and val is not None:
        delete(int(val))
    elif cmd == "list":
        pets_list()
    elif cmd == "stop":
        print("Работа завершена")
        break
    else:
        print("Некорректная команда.")
