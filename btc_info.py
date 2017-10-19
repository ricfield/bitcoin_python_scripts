import urllib, json, ssl, time
from http.client import HTTPSConnection

method = "GET"
currency_pair = "BTC/USD"
url_path = "https://cex.io/api/ticker/" + currency_pair
hostname = "cex.io"
count = 0
exit_loop = True
run = True
delay = 1

btc_api_conn = HTTPSConnection(hostname)

print("Time                 Bid        Ask        Currency Pair")
print("===================  =========  =========  =============")

while run == True:

   btc_api_conn.request(method, url_path)
   btc_api_conn01_response = btc_api_conn.getresponse()
   btc_json_data = json.loads(btc_api_conn01_response.read())
   bid = str('{:8.4f}'.format(btc_json_data['bid']))
   ask = str('{:8.4f}'.format(btc_json_data['ask']))
   time.sleep(delay)

   current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(btc_json_data['timestamp'])))
   print(current_time + "  " + bid + "  " + ask + "  " + currency_pair)

   count += 1

   if count % 100 == 0:

       while exit_loop == True:
          answer = input("Continue running program?(Y/N): ")

          if answer == "Y":
             exit_loop = False
             run = True
          elif answer == "N":
             exit_loop = False
             run = False
          elif answer == "y":
             exit_loop = False
             run = True    
          elif answer == "n":
             exit_loop = False
             run = False            
          else:
             exit_loop == True
             print("INVALID KEY!\n")

       exit_loop = True
  
