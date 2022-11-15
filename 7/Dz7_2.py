"""
2. Римские цифры
Дано: целое число (int).

Задание: Римские цифры пришли к нам из древней римской системы счета. Они основаны на особых буквах алфавита, которые в
различных сочетаниях, путем суммирования (а иногда и разницы) описывают различные числа. Первые 10 римских чисел это:

I, II, III, IV, V, VI, VII, VIII, IX, and X.

Римская система счета имеет десятичное основание, но она непозиционная и не включает в себя 0 (ноль). Римские числа
образуются путем комбинации следующих семи символов:

Символ Значение I 1 (unus) V 5 (quinque) X 10 (decem) L 50 (quinquaginta) C 100 (centum) D 500 (quingenti)
M 1,000 (mille) Узнать больше о римских цифрах вы можете в статье на Википедии.

В этой задаче, вам необходимо преобразовать данное целое число (от 1 до 3999) в римскую систему счета.
"""


def main():
    num_in = input("Введите число\n>> ")
    num = int(num_in)
    rim_num = ""

    while num >= 1000:
        rim_num += "M"
        num -= 1000

    if num >= 900:
        rim_num += "CM"
        num -= 900

    if num >= 500:
        rim_num += "D"
        num -= 500

    if num >= 400:
        rim_num += "CD"
        num -= 400

    while num >= 100:
        rim_num += "C"
        num -= 100

    if num >= 90:
        rim_num += "XC"
        num -= 90

    if num >= 50:
        rim_num += "L"
        num -= 50

    if num >= 40:
        rim_num += "XL"
        num -= 40

    while num >= 10:
        rim_num += "X"
        num -= 10

    if num >= 9:
        rim_num += "IX"
        num -= 9

    if num >= 5:
        rim_num += "V"
        num -= 5

    if num >= 4:
        rim_num += "IV"
        num -= 4

    while num >= 1:
        rim_num += "I"
        num -= 1

    print(f"x = {num_in}, результат: \'{rim_num}\'")


if __name__ == "__main__":
    main()
