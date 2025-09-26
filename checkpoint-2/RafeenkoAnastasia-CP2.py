#Задание 1
birth = int(input("Введите ваш год рождения: "))
year_now = 2025
user_age = year_now - birth
age_after = user_age + 10 
print(f"Ваш текущий возраст: {user_age}")
print(f"Через 10 лет вам будет: {age_after}","\n")
      

# Задание 2
energy = int(input("Введите целое число: "))
if energy % 2 == 0:
    print(f"Число {energy} является четным.")
else:
    print(f"Число {energy} является нечетным.","\n")

# Задание 3 
num = int(input("Введите исходные координаты:"))
print(f"Исходное число: {num}")
print(f"Результат сдвига влево: {num << 2}")
print(f"Результат сдвига вправо: {num >> 1}","\n")

#Задание 4
register = int(input("Введите значение системного регистра:"))
bit_number = int(input("Введите номер бита для проверки (начиная с 0): "))
if bit_number < 0 or bit_number > 31:
    print(f"ошибка")
if register & (1 << bit_number):
    print(f"Бит {bit_number} установлен (значение 1)")
else: 
    print(f"Бит {bit_number} сброшен (значение 0)", "\n")

