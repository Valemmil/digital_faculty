"""
3. Округление
Дано: число с плавающей точкой.

Задание: написать программу, которая будет округлять заданное число:

1) 2-х знаков после запятой; 2) до целого; 3) дополнять слева столько нулей, сколько не хватает числу до 11 знаков.
"""


def main():
    x = float(input("x = "))
    print(f"1) {x:.2f}\n2) {int(x)}\n3) {x:0>11}")


if __name__ == "__main__":
    main()
