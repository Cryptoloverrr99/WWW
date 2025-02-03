import aiohttp
import asyncio
from config import DEXSCREENER_API_URL

class DexScreenerClient:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    async def fetch_new_tokens(self):
        async with aiohttp.ClientSession() as session:
            for attempt in range(5):  # Nouveau : système de retry
                try:
                    async with session.get(
                        DEXSCREENER_API_URL,
                        headers=self.headers,
                        timeout=10
                    ) as response:
                        if response.status == 429:  # Gestion spécifique du 429
                            wait_time = 2 ** (attempt + 1)
                            print(f"Rate limited. Waiting {wait_time}s")
                            await asyncio.sleep(wait_time)
                            continue
                            
                        content_type = response.headers.get('Content-Type', '')
                        if 'application/json' not in content_type:  # Vérification du Content-Type
                            return []
                            
                        data = await response.json()
                        return data.get('tokenProfiles', []) if isinstance(data, dict) else []
                        
                except Exception as e:
                    print(f"API Error: {str(e)}")
                    await asyncio.sleep(30)
            return []
