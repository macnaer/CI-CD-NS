import requests

FILENAME = "currency.txt"

URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"


def get_data(URL):
    responce = requests.get(URL)
    data = responce.json()
    save_to_currency_file(data)
    show_currencies(data)


def save_to_currency_file(data):
    print("dtata => ", data)
    with open(FILENAME, "w") as file:
        for item in data:
            file.write(item["ccy"] + " " + item["base_ccy"] +
                       " " + item["buy"] + " " + item["sale"] + "\n")


def show_currencies(currency):
    for item in currency:
        print(item["ccy"] + " " + item["base_ccy"] +
              " " + item["buy"] + " | " + item["sale"])


get_data(URL)
