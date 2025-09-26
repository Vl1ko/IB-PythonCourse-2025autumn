coordinates = int(input("Введите исходные координаты: "))
shift_on_two = coordinates << 2
shift_on_one = coordinates >> 1
print("Исходное число:", coordinates)
print("Побитовый сдвиг влево на 2 (", coordinates," << 2): ", shift_on_two,sep = "")
print("Побитовый сдвиг влево на 1 (", coordinates," >> 1): ", shift_on_one,sep = "")