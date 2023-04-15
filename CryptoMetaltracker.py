import requests
import json
import tkinter as tk

def fetch_data(api_key, symbols):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {'X-CMC_PRO_API_KEY': api_key}
    params = {'symbol': symbols}
    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.text)
    return data['data']

def fetch_metal_data():
    url = 'https://www.goldapi.io/api/XAU/USD'
    headers = {'x-access-token': 'your_access_token_here'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    gold_price = data['price']
    
    url = 'https://www.goldapi.io/api/XAG/USD'
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    silver_price = data['price']
    
    return gold_price, silver_price

def update_data():
    data = fetch_data(api_key, 'BTC,ETH,XRP,BCH,LTC,XAU,XAG')
    btc_price.config(text=data['BTC']['quote']['USD']['price'])
    eth_price.config(text=data['ETH']['quote']['USD']['price'])
    xrp_price.config(text=data['XRP']['quote']['USD']['price'])
    bch_price.config(text=data['BCH']['quote']['USD']['price'])
    ltc_price.config(text=data['LTC']['quote']['USD']['price'])
    gold_price.config(text=data['XAU']['quote']['USD']['price'])
    silver_price.config(text=data['XAG']['quote']['USD']['price'])
    

    
    root.after(5000, update_data)



def update_prices():
    update_data()

root = tk.Tk()
root.title('Crypto and Metal Price Tracker Ingo Tolle ©2023')

btc_label = tk.Label(root, text='BTC: ')
btc_label.grid(row=0, column=0)
btc_price = tk.Label(root, text='N/A')
btc_price.grid(row=0, column=1)

eth_label = tk.Label(root, text='ETH: ')
eth_label.grid(row=1, column=0)
eth_price = tk.Label(root, text='N/A')
eth_price.grid(row=1, column=1)

xrp_label = tk.Label(root, text='XRP: ')
xrp_label.grid(row=2, column=0)
xrp_price = tk.Label(root, text='N/A')
xrp_price.grid(row=2, column=1)

bch_label = tk.Label(root, text='BCH: ')
bch_label.grid(row=3, column=0)
bch_price = tk.Label(root, text='N/A')
bch_price.grid(row=3, column=1)

ltc_label = tk.Label(root, text='LTC: ')
ltc_label.grid(row=4, column=0)
ltc_price = tk.Label(root, text='N/A')
ltc_price.grid(row=4, column=1)

gold_label = tk.Label(root, text='GOLD: ')
gold_label.grid(row=5, column=0)
gold_price = tk.Label(root, text='N/A')
gold_price.grid(row=5, column=1)

silver_label = tk.Label(root, text='SILVER: ')
silver_label.grid(row=6, column=0)
silver_price = tk.Label(root, text='N/A')
silver_price.grid(row=6, column=1)

update_prices_button = tk.Button(root, text="Update Prices", command=update_prices)
update_prices_button.grid(row=7, column=0, columnspan=2)

api_key = '297a5c9d-8628-446b-8560-19811091ed14'
update_data()
root.geometry("450x300")
root.configure(bg='#4f4f4f')
root.mainloop()