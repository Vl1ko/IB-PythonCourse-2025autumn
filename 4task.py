num = int(input("Введите значение системного регистра: "))
numbit = int(input("Введите номер бита для проверки: "))
if (num>>numberbit) & 1:
    print("Бит", numbit, "установлен(1)")
else:
    print("Бит", numbit, "сброшен(0)")