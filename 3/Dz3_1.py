"""
1. Welcome to Python
Дано: имя и фамилия.

Задание: написать программу, которая будет приветствовать нового человека в мире Python.
         Текст приветсвия: Hello NAME SURNAME! You just delved into Python. Great start!

Пример: Hello Ibrahim Petrov! You just delved into Python. Great start!
"""


def main():
    name = input("Введите ваше имя и фамилию: ")
    print(f"Hello {name}! You just delved into Python. Great start!")


if __name__ == "__main__":
    main()
