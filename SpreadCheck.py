from time import *

import requests


def compare_markets(market_sell1, market_sell2, market_buy):
    # Requests
    # -------------------------------------------------------------------------------------------------
    parameters1 = {"market": market_sell1, "type": "sell"}
    response1 = requests.get(url, params=parameters1)

    parameters2 = {"market": market_sell2, "type": "sell"}
    response2 = requests.get(url, params=parameters2)

    parameters3 = {"market": market_buy, "type": "buy"}
    response3 = requests.get(url, params=parameters3)

    data1 = response1.json()
    data2 = response2.json()
    data3 = response3.json()

    # BTC/ETH (Sell Order)
    # ------------------------------------------------------------------------------------------------
    for x in range(0, AmountResults):
        Quantity1 = data1['result'][x]['Quantity']
        Rate1 = data1['result'][x]['Rate']

        # ETH/COIN (Sell Order)
        # ------------------------------------------------------------------------------------------------
        Quantity2 = data2['result'][x]['Quantity']
        Rate2 = data2['result'][x]['Rate']

        # BTC/COIN (Buy Order)
        # -------------------------------------------------------------------------------------------------
        Quantity3 = data3['result'][x]['Quantity']
        Rate3 = data3['result'][x]['Rate']

        # Spread
        # --------------------------------------------------------------------------------------------------
        Spread = ((N * Rate3 * 100) / (N * Rate2 * Rate1))

        # Condition Volume 1st Order
        # --------------------------------------------------------------------------------------------------
        TestCondition1 = (StackValue <= Rate1 * Quantity1) and (StackValue <= Rate2 * Quantity2) and (
                StackValue <= Rate3 * Quantity3)
        print(Market, " ", Spread, " ", TestCondition1, " ", strftime("%d-%m-%Y %H:%M:%S", gmtime()))
        f = open(Market + ".txt", 'a')
        f.write(Market + " " + str(Spread) + " " + str(TestCondition1) + " " + strftime("%d-%m-%Y %H:%M:%S",
                                                                                        gmtime()) + "\n")
        f.close()


AmountResults = 1
N = 1
StackValue = 0.001

Market = input("Currency to search: ")
marketSell1 = "BTC-ETH"
marketSell2 = "ETH-" + Market
marketBuy = "BTC-" + Market

url = "https://bittrex.com/api/v1.1/public/getorderbook"

try:
    while True:
        compare_markets(marketSell1, marketSell2, marketBuy)

        sleep(60)
except KeyboardInterrupt:
    pass
