from telegram import Bot
from telegram.constants import ParseMode
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

class TelegramAlert:
    def __init__(self):
        self.bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
    async def send_alert(self, token):
        message = (
            "🚨 **New Memecoin Alert!** 🚨\n\n"
            f"🔹 *Token*: {token['name']} ({token['symbol']})\n"
            f"🔹 *Price*: ${token['price']}\n"
            f"🔹 *MCap*: ${token['marketCap']}\n"
            f"🔹 *Liquidity*: ${token['liquidity']}\n"
            f"🔹 *Locked*: {token['liquidityLockedPercent']}%\n"
            f"🔹 *Boosted*: {'✅' if token['boosted'] else '❌'}\n"
            f"🔹 *Ads*: {'✅' if token['ads'] else '❌'}\n"
            "📊 [View on DexScreener]({token['url']})"
        )
        
        await self.bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text=message,
            parse_mode=ParseMode.MARKDOWN_V2,
            disable_web_page_preview=True
        )
