import requests
from boto3.session import Session
import boto3
from lib.Settings import FILENAME, URL

if __name__ == "__main__":
    pass

class Currency:
    def start(self):
        print("Start getting currencies ...")
        self.__get_data(URL)
    
    def __get_data(self,URL):
        responce = requests.get(URL)
        data = responce.json()
        print("data => ", data)
        print("Try to save file")
        self.__save_to_currency_file(data)
        print("Try to show data")
        self.__show_currencies(data)


    def __save_to_s3(self):
        # bucketname = input("Enter bucket name to upload > ")
        bucketname = "currency-u"
        # file_name = input("Enter file name to upload > ")
        file_name = "currency.txt"
        s3 = boto3.client('s3')
        s3.upload_file(file_name, bucketname, file_name)

    def __save_to_currency_file(self, data):
        with open(FILENAME, "w") as file:
            for item in data:
                file.write(item["ccy"] + " " + item["base_ccy"] +
                        " " + item["buy"] + " " + item["sale"] + "\n")
        self.__save_to_s3()

    def __show_currencies(self, currency):
        print("Inside show_Ccurrency")
        for item in currency:
            print(item["ccy"] + " " + item["base_ccy"] +
                " " + item["buy"] + " | " + item["sale"])
              




