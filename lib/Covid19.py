if __name__ == "__main__":
    pass

import requests
from lib.Settings import URL_COVID19, HOSTNAME, USER, PASSWORD
import mysql.connector


class Covid19:

    def __init__(self):
        self.db = mysql.connector.connect(
            host=HOSTNAME,
            user=USER,
            password=PASSWORD
        )
        print(self.db)

    def start(self):

        self.__get_data(URL_COVID19)

    def __get_data(self, URL):
        responce = requests.get(URL_COVID19)
        countries = responce.json()
        for country in countries['Countries']:
            print(country['Country'], "\t\t", country['CountryCode'],
                  country["Slug"], country['NewConfirmed'],
                  country['TotalConfirmed'], country['NewDeaths'],
                  country['TotalDeaths'], country['NewRecovered'],
                  country['TotalRecovered'], country['Date'])

        self.__save_data(countries)

    def __save_data(self, countries):
        cursor = self.db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS covid19")
        cursor.execute('USE covid19')
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS covid19_table (id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255), CountryCode VARCHAR(255),  Slug VARCHAR(255), NewConfirmed INT(10), TotalConfirmed INT(10), NewDeaths INT(10), TotalDeaths INT(10), NewRecovered INT(10), TotalRecovered INT(10), Date DATETIME)")

        # for country in countries['Countries']:
        # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        # val = ("John", "Highway 21")
        # cursor.execute(sql, val)

        # self.db.commit()
