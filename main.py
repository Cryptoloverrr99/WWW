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
                print(f"\n[{datetime.utcnow().isoformat()}] Starting scan cycle")
                
                # Récupération avec logging
                tokens = await self.client.fetch_new_tokens()
                print(f"Received {len(tokens)} tokens from API")
                
                valid_count = 0
                for token in tokens:
                 if isinstance(token, list):  
                for subtoken in token:
            self.process_token(subtoken)
  else:
        self.process_token(token)

                def process_token(self, token):
                 if not isinstance(token, dict):
                     print(f"Invalid token type: {type(token)}")
                     return
    
                for token in tokens:
                    # Vérification cruciale du type
                    if not isinstance(token, dict):
                        print("Skipping invalid token format")
                        continue
                        
                    token_id = token.get('id')
                    if not token_id:
                        continue
                        
                    if token_id not in self.checked_tokens:
                        if check_token(token):
                            valid_count += 1
                            print(f"Valid token found: {token.get('symbol')}")
                            await self.alert.send_alert(token)
                            self.checked_tokens.add(token_id)
                            
                print(f"Cycle completed. Found {valid_count} valid tokens")
                await asyncio.sleep(120)
                
            except Exception as e:
                print(f"FATAL ERROR: {str(e)}")
                await asyncio.sleep(300)

if __name__ == "__main__":
    tracker = MemecoinTracker()
    asyncio.run(tracker.run_cycle())
