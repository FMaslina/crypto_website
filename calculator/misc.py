import requests


def get_exchange_rate() -> float or None:
    url = "https://api.blockchain.com/v3/exchange/tickers/USDT-USD"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            rate = data['last_trade_price']
            return rate
        else:
            return None

    except Exception as e:
        return "Error"
