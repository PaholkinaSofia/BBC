def level_1(stroka, method):
    if method == "upper":
        result = stroka.upper()
    elif method == "lower":
        result = stroka.lower()
    elif method == "capitalize":
        result = stroka.capitalize()
    else:
        result = "нет такого метода выбери другой"
    return str(result)

def level_2(stroka, method):
    if method == "find":
        result = stroka.find("круто")
    elif method == "replace":
        result = stroka.replace("круто", "ок")
    elif method == "count":
        result = stroka.count("о")
    else:
        result = "нет такого метода выбери другой"
    return str(result)

def level_3(stroka, method):
    if method == "split":
        result = stroka.split(",")
        return f"Результат: {result}"
    elif method == "join":
        parts = stroka.split(",")
        result = ",".join(parts)
        return f"Результат: {result}"
    else:
        return "нет иакого метода вебери другой"

def level_4(stroka, method):
    if method == "isdigit":
        result = stroka.isdigit()
    elif method == "isalpha":
        result = stroka.isalpha()
    elif method == "strip":
        result = stroka.strip()
    elif method == "lstrip":
        result = stroka.lstrip()
    elif method == "rstrip":
        result = stroka.rstrip()
    elif method == "format":
        name = input("Введите имя для форматирования: ")
        result = stroka.format(name=name)
    else:
        return "нет такого метода выбери другой"
    return str(result)

def level_5(stroka, method):
    if method == "vse":
        step1 = stroka.strip()
        step2 = step1.replace(";", " ")
        step3 = step2.lower()
        step4 = step3.replace("!", "")
        step5 = step4.capitalize()
        result = step5
        return f"Результат: {result}"
    else:
        return "нет такого метода выбери другой"

def string_game():
    print("Выберите уровень 1-5,введите строку и метод ")
    level_input = input("Уровень 1 2 3 4 5: ")
    level = int(level_input)
    
    if level not in [1, 2, 3, 4, 5]:
        print("уровень должен быть от 1 до5")
        return
    
    stroka = input("Ваша строка: ")
    
    if level == 1:
        print("Методы: upper, lower, capitalize")
    elif level == 2:
        print("Методы: find, replace, count")
    elif level == 3:
        print("Методы: split, join")
    elif level == 4:
        print("Методы: isdigit, isalpha, strip, lstrip, rstrip, format")
    elif level == 5:
        print("Методы: vse")
    
    method = input("Метод: ")
    
    print(f"Уровень {level}: '{stroka}' - {method}")
    
    if level == 1:
        result = level_1(stroka, method)
    elif level == 2:
        result = level_2(stroka, method)
    elif level == 3:
        result = level_3(stroka, method)
    elif level == 4:
        result = level_4(stroka, method)
    elif level == 5:
        result = level_5(stroka, method)
    
    print(f"Результат: {result}")

string_game()
