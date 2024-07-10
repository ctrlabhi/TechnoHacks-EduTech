import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return None

    rates = data.get('conversion_rates')
    if not rates:
        return None

    return rates.get(target_currency)

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    api_key = 'your_api_key_here'  # Replace with your API key
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    amount = float(input(f"Enter amount in {base_currency}: "))

    exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
    if exchange_rate is None:
        print("Error fetching exchange rate.")
        return

    converted_amount = convert_currency(amount, exchange_rate)
    print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}.")

if __name__ == "__main__":
    main()
