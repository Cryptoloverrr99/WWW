import asyncio
from datetime import datetime
from dexscreener_client import DexScreenerClient
from token_filters import check_token
from telegram_bot import TelegramAlert

class MemecoinTracker:
    def __init__(self):
        self.client = DexScreenerClient()
        self.alert = TelegramAlert()
        self.checked_tokens = set()

    async def run_cycle(self):
        while True:
            try:
                tokens = await self.client.fetch_new_tokens()
                for token in tokens:
                    if token['id'] not in self.checked_tokens:
                        if check_token(token):
                            await self.alert.send_alert(token)
                            self.checked_tokens.add(token['id'])
                await asyncio.sleep(120)  # 2 minutes
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    tracker = MemecoinTracker()
    asyncio.run(tracker.run_cycle())
