"""
Дано: словарь ФИО - номер телефона(dict).

Задание: получить новый словарь, инвертировав исходный, т.е. пары ключ - значение поменять местами (значение - ключ).
"""


def main():
    book = {'Petr': '546810', 'Katya': '241815'}
    reversed_book = {}

    for name, num in book.items():
        reversed_book[num] = name

    print("book = {0}\n result = {1}".format(book, reversed_book))


if __name__ == "__main__":
    main()
