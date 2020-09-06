from lib.Currency import Currency
import time

currency = Currency()

counter = 0
while True:
    counter+=1
    print("Get online data => ", counter, " times")
    currency.start()
    time.sleep(300)

