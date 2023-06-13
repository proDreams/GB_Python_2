# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

START_RAND = 0
END_RAND = 1001
FIRST_TRY = 1
LAST_TRY = 11

secret = randint(START_RAND, END_RAND)
for i in range(FIRST_TRY, LAST_TRY):
    n = int(input(f"Попытка номер {i}, попытайтесь отгадать число: "))
    turn = ""
    if n > secret:
        turn = "Меньше"
    elif n < secret:
        turn = "Больше"
    else:
        turn = "Победа!"
        break
    print(turn)
