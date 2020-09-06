import requests
from boto3.session import Session
import boto3
import time

FILENAME = "currency.txt"

URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"


def get_data(URL):
    responce = requests.get(URL)
    data = responce.json()
    print("data => ", data)
    print("Try to save file")
    save_to_currency_file(data)
    print("Try to show data")
    show_currencies(data)


def save_to_s3():
    # bucketname = input("Enter bucket name to upload > ")
    bucketname = "currency-u"
    # file_name = input("Enter file name to upload > ")
    file_name = "currency.txt"
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucketname, file_name)


def save_to_currency_file(data):
    with open(FILENAME, "w") as file:
        for item in data:
            file.write(item["ccy"] + " " + item["base_ccy"] +
                       " " + item["buy"] + " " + item["sale"] + "\n")
    save_to_s3()


def show_currencies(currency):
    print("Inside show_Ccurrency")
    for item in currency:
        print(item["ccy"] + " " + item["base_ccy"] +
              " " + item["buy"] + " | " + item["sale"])


counter = 0
while True:
    counter+=1
    print("Get online data => ", counter, " times")
    get_data(URL)
    time.sleep(300)

