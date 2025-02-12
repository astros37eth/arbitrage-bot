# Arbitrage Bot

This project is an arbitrage bot that monitors price differences between decentralized exchanges (DEX) and centralized exchanges (CEX) and sends notifications when an arbitrage opportunity is found.

## Features

- Monitor prices of ETH on Sushiswap (DEX) and Bybit/Mexc (CEX)
- Compare prices and identify arbitrage opportunities
- Send email notifications when an arbitrage opportunity is detected

## Requirements

- Python 3.x
- `ccxt` library for connecting to CEX
- `web3.py` library for interacting with DEX
- `requests` library for making HTTP requests
- `smtplib` and `email` libraries for sending email notifications

## Installation

1. Clone the repository:

```sh
git clone https://github.com/astros37eth/arbitrage-bot.git
cd arbitrage-bot