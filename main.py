class CurrencyConverter:
    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    def convert_to_usd(self, amount, currency):
        if currency in self.exchange_rates:
            exchange_rate = self.exchange_rates[currency]
            usd_amount = amount / exchange_rate
            return usd_amount
        else:
            return None

exchange_rates = {'UAH': 38}

converter = CurrencyConverter(exchange_rates)

amount_str = input("Введіть кількість валюти: ")
currency_code = input("Введіть код валюти (наприклад, UAH): ")

try:
    amount = float(amount_str)
except ValueError:
    print("Некоректна кількість валюти.")
    exit()

usd_amount = converter.convert_to_usd(amount, currency_code)
if usd_amount is not None:
    print(f"{amount} {currency_code} = {usd_amount:.2f} USD")
else:
    print("Курс валюти не знайдено.")