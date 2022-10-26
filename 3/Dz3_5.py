"""
[Junior] 5. Дизайнер ковриков
Дизайнер составил шаблон домашних ковриков. Для массового выпуска ковриков ему нужно уметь быстро составлять макет
произвольного размера. Известно, что длина коврика всегда больше в 3 раза чем его ширина (W = 3 * H).

Дано: ширина коврика.

Задание: написать программу, которая будет составлять макет коврика для его дальнейшего производства.
"""


def odd(width, heigth, paint):
    for i in range((width-1)//2):
        print((paint*((i*2)+1)).center(heigth, "-"))

    print("WELCOM".center(heigth, "-"))

    for i in range((width-1)//2):
        negativ = (width-1)//2 - i - 1
        print((paint * ((negativ * 2) + 1)).center(heigth, "-"))


def even(width, heigth, paint):
    for i in range(width//2):
        print((paint*((i*2)+1)).center(heigth, "-"))

    for i in range((width-1) // 2):
        negativ = (width-1)//2 - i - 1
        print((paint * ((negativ * 2) + 1)).center(heigth, "-"))


def main():
    width = int(input("Введите ширину ковра: "))
    heigth = width * 3
    paint = ".|."

    print(f"Size: {width} x {heigth}")

    if width % 2 == 0:
        even(width, heigth, paint)
    else:
        odd(width, heigth, paint)


if __name__ == "__main__":
    main()
