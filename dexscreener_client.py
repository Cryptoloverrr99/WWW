import aiohttp
import asyncio
from config import DEXSCREENER_API_URL

class DexScreenerClient:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    async def fetch_new_tokens(self):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(
                DEXSCREENER_API_URL,
                headers=self.headers,
                timeout=10
            ) as response:
                
                # Debug: Afficher la réponse brute
                raw_data = await response.text()
                print(f"API Response: {raw_data[:200]}...")  # Affiche les 200 premiers caractères

                data = await response.json()
                
                # Correction structure réponse API
                if isinstance(data, list):  # Si réponse directe en liste
                    return data
                elif isinstance(data, dict):  # Si réponse avec tokenProfiles
                    return data.get('tokenProfiles', [])
                return []
                
        except Exception as e:
            print(f"API Error: {str(e)}")
            return []
