# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

CONST_HEX = 16


def dec_to_hex(num: int):
    result = []
    alp = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while num > 0:
        result.append(str(alp[num % CONST_HEX]))
        num //= CONST_HEX
    return "".join(result[::-1])


number: int = int(input("Введите число: "))
num_hex: str = dec_to_hex(number)

print(f"""
Число: {number}

Шестнадцатеричное представление: {num_hex}
Проверочное: {hex(number)}""")
