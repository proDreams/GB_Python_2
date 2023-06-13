FOUR_YEARS = 4
HUNDRED_YEARS = 100
FOUR_HUNDRED_YEARS = 400

year = int(input('Введите год в формате yyyy: '))
year_type = ''
if year % FOUR_YEARS != 0 or year % HUNDRED_YEARS == 0 and year % FOUR_HUNDRED_YEARS != 0:
    year_type = 'Обычный'
else:
    year_type = 'Високосный'

print(year_type)
