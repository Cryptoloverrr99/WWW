import requests
from config import DEXSCREENER_API_URL

class DexScreenerClient:
    def get_tokens(self):
        try:
            response = requests.get(DEXSCREENER_API_URL, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
            return response.json() if isinstance(response.json(), list) else []
        except Exception as e:
            print(f"HTTP Error: {str(e)}")
            return []
