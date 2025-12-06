import math

class Calculator:
    
    def arithmetic(body, pervoechislo, vtoroechislo, operation):
        pervoechislo_float = float(pervoechislo)
        vtoroechislo_float = float(vtoroechislo)
        
        if operation == '+':
            result = pervoechislo_float + vtoroechislo_float
        elif operation == '-':
            result = pervoechislo_float - vtoroechislo_float
        elif operation == '*':
            result = pervoechislo_float * vtoroechislo_float
        elif operation == '/':
            result = pervoechislo_float / vtoroechislo_float
        else:
            return "нет такой операции выбери другую"
        
        return float(result)
    
    def trigonometric(body, angle, function):
        angle_float = float(angle)
        
        if function == 'sin':
            result = math.sin(angle_float)
        elif function == 'cos':
            result = math.cos(angle_float)
        elif function == 'tan':
            result = math.tan(angle_float)
        else:
            return "нет такой функции выбери другую"
        return float(result)
    
    def run(body):
        print("Выбери режим калькулятора:")
        print("1 Арифметические операции(+-*/) на 0 деление не поддерживается ")
        print("2 Тригонометрические функции(sin cos tg)")
        
        mode = input("Введите 1 или 2: ")
        
        if mode == "1":
            pervoechislo = input("Введите первое число: ")
            vtoroechislo = input("Введите второе число: ")
            operation = input("Введите операцию (+, -, *, /): ")
            
            result = body.arithmetic(pervoechislo, vtoroechislo, operation)
            print(f"{pervoechislo} {operation} {vtoroechislo} = {result}")
            
        elif mode == "2":
            angle = input("Введите угол в радианах ")
            function = input("Введите функцию (sin, cos, tg) ")
            
            result = body.trigonometric(angle, function)
            print(f"{function}({angle}) = {result}")
            
        else:
            print("нет такого режима надо 1 или 2 выбрать")

calc = Calculator()
calc.run()
