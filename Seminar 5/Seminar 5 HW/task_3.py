# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibonacci():
    fib_1 = 1
    fib_2 = 1
    while True:
        fib_sum = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_sum
        yield fib_sum


for e, fib in enumerate(fibonacci(), start=1):
    print(fib)
    if e == 10:
        break

# fib_it = iter(fibonacci())
# print(next(fib_it))
# print(next(fib_it))
# print(next(fib_it))
# print(next(fib_it))
