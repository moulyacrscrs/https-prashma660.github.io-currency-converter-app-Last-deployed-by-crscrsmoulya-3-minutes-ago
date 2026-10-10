import requests

amount = float(input("Enter amount: "))
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()

url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

response = requests.get(url)
data = response.json()

if to_currency in data["rates"]:
    rate = data["rates"][to_currency]
    converted = amount * rate
    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
else:
    print("Invalid currency code!")