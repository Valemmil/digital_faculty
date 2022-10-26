"""
2. Python art
Дано: маркер (символ) и толщина фигуры.

Задание: написать программу, которая будет отображать заданную фигуру.

Пример: Маркер = H, толщина 5.
"""


def main():
    thickness = 5
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print(" " * (thickness - 1 - len(c * i)) + (c * i) + c + (c * i))

    # Top Pillars
    for i in range(thickness + 1):
        print((" "*((thickness-1)//2)) + (c*thickness) + (" " * (thickness * 3)) + (c*thickness))

    # Middle Belt
    for i in range((thickness+1)//2):
        print((" "*((thickness-1)//2)) + (c*(thickness*5)))

    # Bottom Pillars
    for i in range(thickness + 1):
        print((" "*((thickness-1)//2)) + (c*thickness) + (" " * (thickness * 3)) + (c*thickness))

    # Bottom Cone
    for i in range(thickness):
        negativ = thickness - i - 1
        print((" "*(thickness*4)) + (" " * (thickness - 1 - len(c * negativ))) + (c * negativ) + c + (c * negativ))


if __name__ == "__main__":
    main()
