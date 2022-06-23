from asyncio import exceptions
import requests
import random
import time


def random_num():
    return int(random.random() * 100 + 1)


def send_random_data(url: str):
    """ data = {
        "data0": random_num(),
        "data1": random_num(),
        "data2": random_num(),
        "data3": random_num(),
    } """

    data = {}

    for id in range(int(random.random() * 10)):
        data[f"data{id}"] = random_num()

    try:

        r = requests.post(url, json=data)

        if not r.status_code == 200:
            print(r.json())
    except requests.exceptions.ConnectionError:
        print("cannot POST data")


if __name__ == "__main__":

    while True:
        send_random_data("http://127.0.0.1:5050/send_data")
        time.sleep(1)
