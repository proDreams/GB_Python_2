# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

CONST_HEX = 16
MAX_DIGIT = 9


def dec_to_hex(num: int):
    result = []
    alp = {10: 'A',
           11: 'B',
           12: 'C',
           13: 'D',
           14: 'E',
           15: 'F'}
    while num > 0:
        if num % CONST_HEX > MAX_DIGIT:
            result.append(str(alp[num % CONST_HEX]))
        else:
            result.append(str(num % CONST_HEX))
        num //= CONST_HEX
    return "".join(result[::-1])


number: int = int(input("Введите число: "))
num_hex: str = dec_to_hex(number)

print(f"""
Число: {number}

Шестнадцатеричное представление: {num_hex}
Проверочное: {hex(number)}""")
