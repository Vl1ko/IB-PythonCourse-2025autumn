#Задание 5
import re

def check_password(password):
    """Проверяет пароль на соответствие заданным критериям безопасности."""

    criteria = {
        "length": (len(password) >= 8, "Длина >= 8 символов"),
        "digit": (re.search(r"\d", password), "Содержит цифру"),
        "upper": (re.search(r"[A-Z]", password), "Содержит букву в верхнем регистре"),
        "lower": (re.search(r"[a-z]", password), "Содержит букву в нижнем регистре"),
        "symbol": (re.search(r"[!@#$%^&*]", password), "Содержит специальный символ"),
    }

    is_valid = True 

    for name, (passed, message) in criteria.items():
        if passed:
            print(f"✓ {message}") 
        else:
            print(f"✗ {message}") 
            is_valid = False 
    if is_valid:
        print("Пароль надежен!")
    else:
        print("Пароль ненадежен!")

    return is_valid

password = input("Введите пароль: ")
check_password(password)
