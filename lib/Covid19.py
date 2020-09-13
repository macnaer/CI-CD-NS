if __name__ == "__main__":
    pass

import requests
from lib.Settings import URL_COVID19


class Covid19:
    def start(self):
        print("Start getting currencies ...")
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
