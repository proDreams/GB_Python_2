# Задача с курса Java Core.
# Предположить, что числа в исходном массиве из 9 элементов имеют диапазон[0, 3], и представляют собой,
# например, состояния ячеек поля для игры в крестики-нолики,
# где 0 – это пустое поле, 1 – это поле с крестиком, 2 – это поле с ноликом, 3 – резервное значение.
# Такое предположение позволит хранить в одном числе типа int всё поле 3х3.
# Записать в файл 9 значений так, чтобы они заняли три байта.
#
#
# В продолжение дописать "разворачивание" поля игры крестики-нолики из сохраненного в файле состояния
# (распарсить файл, в зависимости от значений (0-3) нарисовать поле со значками 'х' 'о' '.')

def compress(rows, res):
    for row in rows:
        res.append((row // 100 * 4 ** 2 + row // 10 % 10 * 4 ** 1 + row % 10 * 4 ** 0).to_bytes(1, 'big'))


def write_file(path, rows):
    with open('test.txt', 'wb') as f:
        for row in rows:
            f.write(row)


def read_file(path, res):
    with open(path, 'rb') as f:
        file = f.read()
        for b in file:
            res.append(b)


def decompress(data):
    res = []
    for num in data:
        temp = []
        while num > 0:
            temp.append(str(num % 4))
            num //=  4
        res.append(int("".join(temp[::-1])))
    return res
def main():
    xo_rows = [333, 333, 333]
    compress_to_byte = []

    compress(xo_rows, compress_to_byte)
    write_file('test.txt', compress_to_byte)

    file_data = []
    read_file('test.txt', file_data)
    decompressed = decompress(file_data)
    print(decompressed)

if __name__ == '__main__':
    main()
