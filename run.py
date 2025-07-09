from src.api import get_crypto_price

def main():
    """
    Main function to run the crypto price tracker.
    Fetches and prints the current prices of Bitcoin and Ethereum in USD and INR.
    """
    try:
        print("🔍 Welcome to Crypto Price Tracker!")
        crypto_id = input("Enter the cryptocurrency ID (e.g., bitcoin, ethereum): ").lower()
        
        price_data = get_crypto_price(crypto_id)
        print(f"\n💰 {crypto_id.upper()} Price:")
        print(f"🇮🇳 INR: ₹{price_data['inr']}")
        print(f"🇺🇸 USD: ${price_data['usd']}\n")

        print("📈 Price fetched successfully!")


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()