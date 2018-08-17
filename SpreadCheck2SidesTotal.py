from time import *

import requests

BTC_ETH_MARKET = "BTC-ETH"
BTC_COIN_MARKET = "BTC-"
ETH_COIN_MARKET = "ETH-"


def get_market_data(market, market_type):
    parameters = {"market": market, "type": market_type}
    response = requests.get(url, params=parameters)
    return response.json()


def get_quantity_rate(data, idx):
    return data['result'][idx]['Quantity'], data['result'][idx]['Rate']


def compare_to_btc_eth_market(market, direction="A"):
    if direction == "A":
        data1 = get_market_data(BTC_ETH_MARKET, "sell")
        data2 = get_market_data(ETH_COIN_MARKET + market, "sell")
        data3 = get_market_data(BTC_COIN_MARKET + market, "buy")
    elif direction == "B":
        data1 = get_market_data(BTC_COIN_MARKET + market, "sell")
        data2 = get_market_data(ETH_COIN_MARKET + market, "buy")
        data3 = get_market_data(BTC_ETH_MARKET, "buy")
    else:
        raise NotImplementedError("Direction %s not implemented" % direction)

    for x in range(0, AmountResults):
        Quantity1, Rate1 = get_quantity_rate(data1, x)
        Quantity2, Rate2 = get_quantity_rate(data2, x)
        Quantity3, Rate3 = get_quantity_rate(data3, x)

        if direction == "A":
            Spread = ((N * Rate3 * 100) / (N * Rate2 * Rate1))
        elif direction == "B":
            Spread = ((N * Rate3 * Rate2 * 100) / (N * Rate1))
        else:
            raise NotImplementedError("Direction %s not implemented" % direction)

        test_condition = (StackValue <= Rate1 * Quantity1) and (StackValue <= Rate2 * Quantity2) and (
                StackValue <= Rate3 * Quantity3)
        output = "Direction %s: %s %f %r %s" % (direction, market, Spread, test_condition,
                                                strftime("%d-%m-%Y %H:%M:%S", gmtime()))

        print(output)
        f = open(Market + ".txt", 'a')
        f.write(output + "\n")
        f.close()


AmountResults = 1
N = 1
StackValue = 0.001

Market = input("Currency to search: ")

url = "https://bittrex.com/api/v1.1/public/getorderbook"

try:
    while True:
        compare_to_btc_eth_market(Market, "A")
        compare_to_btc_eth_market(Market, "B")

        sleep(60)
except KeyboardInterrupt:
    pass
