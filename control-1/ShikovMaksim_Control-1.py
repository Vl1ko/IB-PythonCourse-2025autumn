#Задание 1

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print(f"Сумма: {num1} + {num2} = {num1 + num2}")
print(f"Разность: {num1} - {num2} = {num1 - num2}")
print(f"Произведение: {num1} * {num2} = {num1 * num2}")
print(f"Частное: {num1} / {num2} = {num1 / num2}", end=("\n\n"))


#Задание 2

age = int(input("Введите ваш возраст: "))
med = (input("У вас есть медицинская справка? (Да/Нет): ")).lower()
if age >= 18 and med == "да":
    print("Можно получить права")
elif age >= 18 and med == "нет":
    print("Нужна медицинская справка")
else:
    print("Слишком молод чтобы получить права")


#Задание 3

celnum = int(input("Введите целое число: "))
sdvig1 = celnum << 2
sdvig2 = celnum >> 1
pobit1 = celnum & 15
pobit2 = celnum | 3
print(f"Исходное число: {celnum} - ({celnum:b})")
print(f"Сдвиг в лево на 2: {sdvig1} - ({sdvig1:b})")
print(f"Сдвиг в право на 1: {sdvig2} - ({sdvig2:b})")
print(f"Побитовое И c 15: {pobit1} - ({pobit1:b})")
print(f"Побитовое ИЛИ c 3: {pobit2} - ({pobit2:b})")


#Задани 4

try:
    calcNum1 = float(input("Введите первое число: "))
    calcNum2 = float(input("Введите второе число: "))
    oper = input("Введите операцию (+, -, *, /, %, //): ")

    if oper == "+":
        print(f"Сумма: {calcNum1} + {calcNum2} = {calcNum1 + calcNum2}")
    elif oper == "-":
        print(f"Вычитание: {calcNum1} - {calcNum2} = {calcNum1 - calcNum2}")
    elif oper == "*":
        print(f"Умножение: {calcNum1} * {calcNum2} = {calcNum1 * calcNum2}")
    elif oper == "/":
        print(f"Деление: {calcNum1} / {calcNum2} = {calcNum1 / calcNum2}")
    elif oper == "%":
        print(f"Деление по модулю (остаток от деления): {calcNum1} % {calcNum2} = {calcNum1 % calcNum2}")
    elif oper == "//":
        print(f"Деление без остатка: {calcNum1} // {calcNum2} = {calcNum1 // calcNum2}")
    else:
        print("Неверная операция")
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionError:
    print("На ноль делить низя")


#Задание 5

pas = input("Введите пароль: ")
len = len(pas) >= 8
numbers = any(sim.isdigit() for sim in pas)
upreg = any(sim.isupper() for sim in pas)
lowreg = any(sim.islower() for sim in pas)
spec = any(sim in "!@#$%^&?*" for sim in pas)

if len:
    print("✓ Длина >= 8 символов")
else:
    print("✗ Длина >= 8 символов")
if numbers:
    print("✓ Содержит цифру")
else:
    print("✗ Содержит цифру")
if upreg:
    print("✓ Содержит букву в верхнем регистре")
else:
    print("✗ Содержит букву в верхнем регистре")
if lowreg:
    print("✓ Содержит букву в нижнем регистре")
else:
    print("✗ Содержит букву в нижнем регистре")
if spec:
    print("✓ Содержит специальный символ")
else:
    print("✗ Содержит специальный символ")
if len and numbers and upreg and lowreg and spec:
    print("Пароль надежен!")
else:
    print("Пароль ненадежен")