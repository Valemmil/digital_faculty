"""
2. Max-min
Дано: массив чисел (float или/и int).

Задание: нужно найти разницу между самым большим (максимум) и самым малым (минимум) элементом.
Если список пуст, то результат равен 0 (ноль).

Числа с плавающей точкой представлены в компьютерах как двоичная дробь.
Результат проверяется с точностью до третьего знака, как ±0.001
"""


def main():
    in_num = input("Введите список чисел через ', ': ")
    if in_num != "":
        elements = in_num.split(", ")
    else:
        elements = ["0"]

    try:
        min_num = int(elements[0])
    except ValueError:
        min_num = float(elements[0])

    try:
        max_num = int(elements[0])
    except ValueError:
        max_num = float(elements[0])

    for i in elements:
        try:
            temp = int(i)
        except ValueError:
            temp = float(i)

        if temp < min_num:
            min_num = temp
        if temp > max_num:
            max_num = temp

    print("Результат: {0:.2f}".format(max_num - min_num))


if __name__ == "__main__":
    main()
