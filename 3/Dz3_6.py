"""
[Junior+] 6. Произведение цифр
Дано: целое число.

Задание: написать программу, которая перемножит все цифры заданного числа (0 - исключить).
"""


def main():
    number = int(input("Введите число: "))
    result = 1

    while number != 0:
        if number % 10 != 0:
            result *= number % 10
        number = number // 10

    print(f"result = {result}")


if __name__ == "__main__":
    main()
