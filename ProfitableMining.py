import requests
import time


def get_hash_rate():
    hash_rate = 184 / 1000000  # Convert Mh/s to h/s
    return hash_rate  # Return rate


def get_watts():
    watts = 380  # Power miner uses
    return watts  # Return watts


def get_energy_cost():
    energy_cost = 0.10  # Cost per kWh
    return energy_cost  # Return energy cost


def get_json_file():
    pool = "https://www.litecoinpool.org/api?api_key="  # Litecoinpool stat page
    api_key = ""  # User api key
    url = pool + api_key  # Creates url To get json
    return requests.get(url)  # Return json


def check_if_profitable():
    r = get_json_file()
    litecoin_difficulty = r.json()['network']['difficulty']  # Gets litecoin difficulty
    litecoin_price = r.json()['market']['ltc_usd']  # Gets litecoin price
    power_cost_hr = (((get_watts() * 24) / 1000) * get_energy_cost())  # Calculate cost of running device per day
    reward = (get_hash_rate() * 12.5 * 86400) / (litecoin_difficulty * (2**32))  # Calculate mining reward per day
    net_profit = ((reward * litecoin_price) - power_cost_hr)  # calculate net profit
    if net_profit > 0:  # Check if profitable to mine
        return True  # Profitable
    return False  # Not profitable


def main():
    while True:
        if check_if_profitable():
            print("mining")
        else:
            print("not mining")
        time.sleep(60)  # 5 minute sleep


if __name__ == "__main__":
    main()
