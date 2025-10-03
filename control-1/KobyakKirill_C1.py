
# Задание №1

"""
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print("Сумма чисел:", number1 + number2)
print("Сумма чисел:", number1 - number2)
print("Сумма чисел:", number1 * number2)
print("Сумма чисел:", number1 / number2)"""

# Задание №2

"""
age = int(input("Ваш текущий возраст: "))
medkarta = input("У вас есть мед карта? (Да/Нет) ")
if age < 18:
    print("Слишком молод для получения прав")
elif medkarta == "Да":
    print("Можно получить права!")
else:
    print("Нужна медицинская карта")
"""

# Задание №3

"""
chislo = int(input("Введите целое число: "))
sdvig1 = chislo << 2
sdvig2 = chislo >> 1
pobitovoe1 = chislo & 15
pobitovoe2 = chislo | 3
print(f"Исходное число: {chislo} - ({chislo:b})")
print(f"Сдвиг влево на 2: {sdvig1} - ({sdvig1:b})")
print(f"Сдвиг вправо на 1: {sdvig2} - ({sdvig2:b})")
print(f"Побитовое И c 15: {pobitovoe1} - ({pobitovoe1:b})")
print(f"Побитовое ИЛИ c 3: {pobitovoe2} - ({pobitovoe2:b})")
"""

# Задание №4

"""
try:
    Num1 = float(input("Введите первое число: "))
    Num2 = float(input("Введите второе число: "))
    oper = input("Введите операцию (+, -, *, /, %, //): ")

    if oper == "+":
        print("Сумма:", Num1 + Num2)
    elif oper == "-":
        print("Вычитание", Num1 - Num2)
    elif oper == "*":
        print("Умножение:", Num1 * Num2)
    elif oper == "/":
        print("Деление:", Num1 / Num2)
    elif oper == "%":
        print("Деление по модулю (остаток от деления):", Num1 % Num2)
    elif oper == "//":
        print("Деление без остатка:", Num1 // Num2)
    else:
        print("Неверная операция")
except ValueError:
    print("Ошибка ввода числа, попробуйте другое число!")
except ZeroDivisionError:
    print("На ноль делить нельзя")
"""

# Задание №5

password = input("Введите пароль: ")
len = len(password) >= 8
numbers = any(sim.isdigit() for sim in password)
regUP = any(sim.isupper() for sim in password)
reglow = any(sim.islower() for sim in password)
spec = any(sim in "!@#$%^&?*" for sim in password)

if len:
    print("✓ Длина >= 8 символов")
else:
    print("✗ Длина >= 8 символов")
if numbers:
    print("✓ Содержит цифру")
else:
    print("✗ Содержит цифру")
if regUP:
    print("✓ Содержит букву в верхнем регистре")
else:
    print("✗ Содержит букву в верхнем регистре")
if reglow:
    print("✓ Содержит букву в нижнем регистре")
else:
    print("✗ Содержит букву в нижнем регистре")
if spec:
    print("✓ Содержит специальный символ")
else:
    print("✗ Содержит специальный символ")
if len and numbers and regUP and reglow and spec:
    print("Пароль надежен!")
else:
    print("Пароль ненадежен")