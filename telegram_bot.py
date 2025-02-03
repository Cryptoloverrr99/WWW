from telegram import Bot
from telegram.constants import ParseMode
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

class TelegramAlert:
    def __init__(self):
        self.bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
    async def send_alert(self, token):
        # Protection contre les données manquantes
        message = (
            "🚨 **New Memecoin Alert!** 🚨\n\n"
            f"🔹 *Token*: {token.get('name', 'N/A')} ({token.get('symbol', '?')})\n"
            f"🔹 *Price*: ${token.get('price', 'N/A'):.8f}\n"
            f"🔹 *MCap*: ${token.get('marketCap', 'N/A'):,.2f}\n"
            f"🔹 *Liquidity*: ${token.get('liquidity', 0):,.2f}\n"
            f"🔹 *Locked*: {token.get('liquidityLockedPercent', 0)}%\n"
            f"🔹 *DEX*: {token.get('dex', {}).get('name', 'Unknown')}\n"
            "📊 [View on DexScreener](https://dexscreener.com/)"
        )
        
        await self.bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text=message,
            parse_mode=ParseMode.MARKDOWN_V2,
            disable_web_page_preview=True
                          )
