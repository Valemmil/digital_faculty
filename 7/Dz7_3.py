"""
3. Ленивый спекулянт
Дано: словарь банк - курс доллара (dict).

Задание: определить банк и курс покупки валюты с наиболее привлекательным предложением.
"""


def main():
    rates = {'Sberbank': 55.8, 'VTB24': 53.91}
    min_value = float("inf")
    best_bank = ""
    for bank, value in rates.items():
        if min_value > value:
            min_value = value
            best_bank = bank

    print(f"{best_bank} -> {min_value}")


if __name__ == "__main__":
    main()
