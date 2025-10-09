#Задание 4
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Нужно ввести число!")

num_a = get_number("Введите первое число: ")
num_b = get_number("Введите второе число: ")
operation = input("Введите операцию (+, -, *, /, %, //): ")

if operation not in ['+', '-', '*', '/', '%', '//']:
    print("Ошибка: Неизвестная операция!")
else:
    try:
        if operation == '+':
            result = num_a + num_b
        elif operation == '-':
            result = num_a - num_b
        elif operation == '*':
            result = num_a * num_b
        elif operation == '/':
            result = num_a / num_b
        elif operation == '%':
            result = num_a % num_b  
        elif operation == '//':
            result = num_a // num_b 
            
        print(f"Результат: {num_a} {operation} {num_b} = {result}")

    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
