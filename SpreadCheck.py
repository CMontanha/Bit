import requests
import os
import time
import json
from time import gmtime, strftime


market = input("Market: ")

url = "https://bittrex.com/api/v1.1/public/getorderbook"

try:
 while True:
  #absolutely_unused_variable = os.system("cls")

  #BTC/ETH
  #------------------------------------------------------------------------------------------------
  parameters = {"market": "BTC-ETH", "type": "sell"}
  response = requests.get(url, params = parameters)
  data = response.json()
  Quantity1 = data['result'][0]['Quantity']
  Rate1 = data['result'][0]['Rate']


  #ETH/MARKET
  #------------------------------------------------------------------------------------------------
  parameters = {"market": "ETH-" + market , "type": "sell"}
  response = requests.get(url, params = parameters)
  data = response.json()
  Quantity2 = data['result'][0]['Quantity']
  Rate2 = data['result'][0]['Rate']

  #BTC/MARKET
  #-------------------------------------------------------------------------------------------------
  parameters = {"market": "BTC-" + market , "type": "buy"}
  response = requests.get(url, params = parameters)
  data = response.json()
  Quantity3 = data['result'][0]['Quantity']
  Rate3 = data['result'][0]['Rate']

  #SpreadCalculator
  #--------------------------------------------------------------------------------------------------
  N = 1
  Spread = ((N*Rate3*100)/(N*Rate2*Rate1))
  
  #Condition (Volume 1st Orders)
  #--------------------------------------------------------------------------------------------------
  StackValue = 0.001
  TestCondition1 = (StackValue <= Rate1*Quantity1) and (StackValue <= Rate2*Quantity2) and (StackValue <= Rate3*Quantity3)
  
  print(market, " ", Spread, " ", TestCondition1, " ", strftime("%d-%m-%Y %H:%M:%S", gmtime()))
  f = open(market+".txt", 'a')
  f.write(market + " " + str(Spread) + " " + str(TestCondition1) + " " + strftime("%d-%m-%Y %H:%M:%S", gmtime()) + "\n")
  f.close()

  time.sleep(60)
except KeyboardInterrupt:
 pass