register = int(input("Введите значение системного регистра: "))
bit = int(input("Введите номер бита для проверки: "))
if register & (1 << bit):
    print(f"Бит {bit} установлен (1)")
else:
    print(f"Бит {bit} сброшен (0)")