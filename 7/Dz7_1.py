"""
1. Анализ текста. Популярность.
Дано: текст (str).

Задание: необходимо получить 2 словаря (популярности слов и популярности букв).
"""


def main():
    text = input("Введите текст\n>> ")
    clear_text = text.replace(",", "").replace(".", "").lower()
    words_popularity = {}
    chars_popularity = {}

    for i in clear_text:
        if i != " ":
            if i not in chars_popularity:
                chars_popularity[i] = 0
            chars_popularity[i] += 1

    words = clear_text.split(" ")

    for i in words:
        if i not in words_popularity:
            words_popularity[i] = 0
        words_popularity[i] += 1

    print("\ntext = \"{}\", результат:".format(text),
          "\n\tchars_popularity = {}".format(chars_popularity),
          "\n\twords_popularity = {}".format(words_popularity))


if __name__ == "__main__":
    main()
