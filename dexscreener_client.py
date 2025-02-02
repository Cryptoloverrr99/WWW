import aiohttp
import asyncio
from config import DEXSCREENER_API_URL

class DexScreenerClient:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    async def fetch_new_tokens(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(DEXSCREENER_API_URL, headers=self.headers) as response:
                data = await response.json()
                return data.get('tokenProfiles', [])
    
    async def get_token_details(self, token_id):
        url = f"https://api.dexscreener.com/latest/dex/tokens/{token_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                return await response.json()
