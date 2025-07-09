import json
import os
from .errors import APIError
from .logger import logger

def get_crypto_price(crypto_id: str) -> dict:
    mock_file = os.path.join(os.path.dirname(__file__), "mock_data.json")

    try:
        with open(mock_file, "r") as f:
            data = json.load(f)

        if crypto_id not in data:
            logger.error(f"{crypto_id} not found in mock data.")
            raise APIError("Cryptocurrency not supported in mock data.")

        logger.info(f"Fetched mock price for: {crypto_id}")
        return data[crypto_id]

    except FileNotFoundError:
        logger.error("mock_data.json not found.")
        raise APIError("Mock data file missing.")
    except Exception as err:
        logger.error(f"Unexpected error: {err}")
        raise APIError("An unexpected error occurred while reading mock data.")
# This function simulates fetching cryptocurrency prices from a mock data file.
# It reads from a JSON file containing mock prices for various cryptocurrencies.   