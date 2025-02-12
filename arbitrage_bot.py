import ccxt
import requests
from web3 import Web3
import time
import smtplib
from email.mime.text import MIMEText

# Set up connection to Ethereum node
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))

# Set up connection to CEX using ccxt
bybit = ccxt.bybit()
mexc = ccxt.mexc()

# Function to get price from Sushiswap (DEX)
def get_sushiswap_price():
    # Replace with actual contract address and ABI
    contract_address = '0x...'
    contract_abi = '...'

    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    price = contract.functions.getPrice().call()
    return web3.fromWei(price, 'ether')

# Function to get price from CEX
def get_cex_price(exchange, symbol):
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

# Function to send email notification
def send_email_notification(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Arbitrage Opportunity'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'your_email@example.com'

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.sendmail('your_email@example.com', 'your_email@example.com', msg.as_string())

# Main loop
while True:
    try:
        sushiswap_price = get_sushiswap_price()
        bybit_price = get_cex_price(bybit, 'ETH/USDT')
        mexc_price = get_cex_price(mexc, 'ETH/USDT')

        if bybit_price - sushiswap_price > 20:
            send_email_notification(f"Arbitrage opportunity: Buy on Sushiswap at ${sushiswap_price} and sell on Bybit at ${bybit_price}")
        if mexc_price - sushiswap_price > 20:
            send_email_notification(f"Arbitrage opportunity: Buy on Sushiswap at ${sushiswap_price} and sell on Mexc at ${mexc_price}")

        time.sleep(60)  # Check prices every minute

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(60)