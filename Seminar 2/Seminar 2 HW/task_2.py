# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
from fractions import Fraction


def gcd(n, d):
    while d:
        n, d = d, n % d
    return n


def check_eq(num, denum):
    if num % denum == 0:
        return num
    gcd_num = gcd(num, denum)
    return f"{num // gcd_num}/{denum // gcd_num}"


def sum_frac(a, b, d_a, d_b):
    new_num_a, new_denum_a = a * d_b, d_a * d_b
    new_num_b, new_denum_b = b * d_a, d_b * d_a
    sum_num = new_num_a + new_num_b
    return check_eq(sum_num, new_denum_b)


def prod_frac(a, b, d_a, d_b):
    num = a * b
    denum = d_a * d_b
    return check_eq(num, denum)


num_a, denum_a = map(int, input("Введите первую дробь вида a/b: ").split("/"))
num_b, denum_b = map(int, input("Введите вторую дробь вида a/b: ").split("/"))

print(f"""Первая дробь: {num_a}/{denum_a}
Вторая дробь: {num_b}/{denum_b}

Сумма дробей: {sum_frac(num_a, num_b, denum_a, denum_b)}
Проверка: {Fraction(num_a, denum_a) + Fraction(num_b, denum_b)}

Произведение дробей: {prod_frac(num_a, num_b, denum_a, denum_b)}
Проверка: {Fraction(num_a, denum_a) * Fraction(num_b, denum_b)}""")
