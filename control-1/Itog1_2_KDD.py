#Задание 2
age = int(input("Ваш возраст:"))
med = input("Есть ли мед. справка(да/нет):").lower()
if age >= 18 and "да" in med:
    print("Можно получить права")
elif age >= 18 and "нет" in med:
    print("Нужна медицинская справка")
else:
     print("Слишком молод для получения прав")