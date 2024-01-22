from forex_python.converter import CurrencyRates, RatesNotAvailableError
from colorama import init, Fore

init(autoreset=True)  # Initialize colorama for autoreset

def get_available_currency_codes():
    c = CurrencyRates()
    return c.get_rates('USD').keys()  # Assuming USD as the base currency

def convert_currency(amount, from_currency, to_currency):
    try:
        c = CurrencyRates()
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount
    except RatesNotAvailableError as e:
        print(f"{Fore.RED}Error: {e}")
        return None

if __name__ == "__main__":
    # Display available currency codes in green
    available_currency_codes = get_available_currency_codes()
    print(f"{Fore.GREEN}Available Currency Codes: {', '.join(available_currency_codes)}")

    # Input values in red
    amount = float(input(f"{Fore.RED}Enter the amount: "))
    from_currency = input(f"{Fore.RED}Enter the source currency code: ").upper()
    to_currency = input(f"{Fore.RED}Enter the target currency code: ").upper()

    # Perform conversion
    result = convert_currency(amount, from_currency, to_currency)

    # Display result or error message in colors
    if result is not None:
        print(f"{Fore.GREEN}{amount} {from_currency} is equal to {result:.2f} {to_currency}")
    else:
        print(f"{Fore.RED}Please check the currency codes and try a different currency pair.")
