import requests
import os
import time
import json
from time import gmtime, strftime


AmountResults = 1
N = 1
StackValue = 0.01

Market = input("Currency to search: ")

#Direction A - BTC-ETH-COIN-BTC
#--------------------------------------------------------------------
marketSell1 = "BTC-ETH"
marketSell2 = "ETH-" + Market
marketBuy = "BTC-" + Market

#Direction B - BTC-COIN-ETH-BTC
#---------------------------------------------------------------------
marketSell3 = "BTC-" + Market
marketBuy2 = "ETH-" + Market
marketBuy3 = "BTC-ETH"

url = "https://bittrex.com/api/v1.1/public/getorderbook"

try:
 while True:
  #absolutely_unused_variable = os.system("cls")
  
  #Requests
  #Direction A - BTC-ETH-COIN-BTC
  #-------------------------------------------------------------------------------------------------
  parameters1 = {"market": marketSell1, "type": "sell"}
  response1 = requests.get(url, params = parameters1)

  parameters2 = {"market": marketSell2, "type": "sell"}
  response2 = requests.get(url, params = parameters2)

  parameters3 = {"market": marketBuy, "type": "buy"}
  response3 = requests.get(url, params = parameters3)

  #Direction B - BTC-COIN-ETH-BTC
  #--------------------------------------------------------------------------------------------------
  parameters4 = {"market": marketSell3, "type": "sell"}
  response4 = requests.get(url, params = parameters4)

  parameters5 = {"market": marketBuy2, "type": "buy"}
  response5 = requests.get(url, params = parameters5)

  parameters6 = {"market": marketBuy3, "type": "buy"}
  response6 = requests.get(url, params = parameters6)
  
  #Data
  #---------------------------------------------------------------------------------------------------
  data1 = response1.json()
  data2 = response2.json()
  data3 = response3.json()
  data4 = response4.json()
  data5 = response5.json()
  data6 = response6.json()

  #Direction A
  #BTC/ETH
  #------------------------------------------------------------------------------------------------
  for x in range(0, AmountResults):
    Quantity1 = data1['result'][x]['Quantity']
    Rate1 = data1['result'][x]['Rate']

  #ETH/COIN
  #------------------------------------------------------------------------------------------------
    Quantity2 = data2['result'][x]['Quantity']
    Rate2 = data2['result'][x]['Rate']

  #BTC/COIN
  #-------------------------------------------------------------------------------------------------
    Quantity3 = data3['result'][x]['Quantity']
    Rate3 = data3['result'][x]['Rate']
  
  #Direction B
  #BTC/COIN
  #-------------------------------------------------------------------------------------------------
    Quantity4 = data4['result'][x]['Quantity']
    Rate4 = data4['result'][x]['Rate']

  #ETH/COIN
  #------------------------------------------------------------------------------------------------
    Quantity5 = data5['result'][x]['Quantity']
    Rate5 = data5['result'][x]['Rate']

  #BTC/ETH
  #-------------------------------------------------------------------------------------------------
    Quantity6 = data6['result'][x]['Quantity']
    Rate6 = data6['result'][x]['Rate']

  #Spread
  #--------------------------------------------------------------------------------------------------
    SpreadA = ((N*Rate3*100)/(N*Rate2*Rate1))
    SpreadB = ((N*Rate4*100)/(N*Rate6*Rate5))
  
  #Condition Volume 1st Order
  #--------------------------------------------------------------------------------------------------
    TestConditionA = (StackValue <= Rate1*Quantity1) and (StackValue <= Rate2*Quantity2) and (StackValue <= Rate3*Quantity3)
    TestConditionB = (StackValue <= Rate4*Quantity4) and (StackValue <= Rate5*Quantity5) and (StackValue <= Rate6*Quantity6)
    print("Direction A", Market, " ", SpreadA, " ", TestConditionA, " ", strftime("%d-%m-%Y %H:%M:%S", gmtime()))
    print("Direction B ", Market, " ", SpreadB, " ", TestConditionB, " ", strftime("%d-%m-%Y %H:%M:%S", gmtime()))
    f = open(Market+".txt", 'a')
    f.write("Direction A" + Market + " " + str(SpreadA) + " " + str(TestConditionA) + " " + strftime("%d-%m-%Y %H:%M:%S", gmtime()) + "\n")
    f.write("Direction B" + Market + " " + str(SpreadB) + " " + str(TestConditionB) + " " + strftime("%d-%m-%Y %H:%M:%S", gmtime()) + "\n")
    f.close()

  time.sleep(60)
except KeyboardInterrupt:
 pass
