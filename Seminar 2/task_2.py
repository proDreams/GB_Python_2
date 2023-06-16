# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно

def bin_octa(num: int, prod: int) -> str:
    result = []
    while num > 0:
        result.append(str(num % prod))
        num //= prod
    return "".join(result[::-1])


CONST_BIN = 2
CONST_OCTA = 8

number: int = int(input("Введите число: "))
num_bin: str = bin_octa(number, CONST_BIN)
num_octa: str = bin_octa(number, CONST_OCTA)

print(f"""
Число: {number}

Двоичное представление: {num_bin}
Проверочное: {bin(number)}

Восьмеричное представление: {num_octa}
Проверочное: {oct(number)}""")
