#Задание 1
user_year = int(input("Введите ваш год рождения:"))
year_now = 2025
years_now = year_now - user_year
years_after = years_now + 10
print("Ваш текущий возвраст:", years_now)
print("Через 10 лет вам будет:", years_after, end=("\n\n"))

#Задание 2
shield_energy = int(input("Введиет уровень энергии: "))
if shield_energy % 2 == 0:
    print("Щит активен")
else:
    print("Щит не активен")

if shield_energy &(1<<0) == 0:
    print("Щит активен")
else:
    print("Щит не активен")

#Задание 3
start_cord = int(input("Введите исходные координаты: "))
print("Исходное число:", start_cord)
print("Побитывай сдвиг влево на 2 (10 << 2):", start_cord<<2)
print("Побитовый сдвиг в право на 1 (10 >> 1):", start_cord>>1, end=("\n\n"))

#Задание 4
sys_reg = int(input("Введите значение системного регистра: "))
sys_byt = int(input("Введите номер бита для проверки: "))
if sys_reg &(1<<sys_byt):
    print("Бит", sys_byt, "установлен (1)")
else:
    print("Бит", sys_byt, "сброшен (0)", end=("\n\n"))