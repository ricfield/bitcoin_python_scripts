import urllib, json, ssl, time
from http.client import HTTPSConnection

method = "GET"
currency_pairs = {"BTCUSD" : "BTC/USD"}
url_path = "https://cex.io/api/ticker/" + currency_pairs["BTCUSD"]
hostname = "cex.io"
exit_loop = True
run = True
delay = 1
btc = {"bid" : "0", "ask" : "0"}


def main():
   
   btc_api_conn = HTTPSConnection(hostname)

   print("\nTime                 Bid        Ask        Currency Pair")
   print("===================  =========  =========  =============")

   while run == True:
      btc_api_conn.request(method, url_path)
      btc_api_conn01_response = btc_api_conn.getresponse()
      btc_json_data = json.loads(btc_api_conn01_response.read())
      btc["bid"] = str('{:8.4f}'.format(btc_json_data['bid']))
      btc["ask"] = str('{:8.4f}'.format(btc_json_data['ask']))
      time.sleep(delay)

      current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(btc_json_data['timestamp'])))
      print(current_time + "  " + btc["bid"] + "  " + btc["ask"] + "  " + currency_pairs["BTCUSD"], end = "\r")

if __name__ == '__main__':
   main()
   
