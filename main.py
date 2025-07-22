import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TOKEN
from signals import get_market_signal
from news_scraper import get_latest_news

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привіт! Я трейдинг-бот. Надішли /signal, /price або /news.")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signal = get_market_signal()
    await update.message.reply_text(f"📊 Сигнал ринку: {variable}") 
{signal}")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from signals import get_current_price
    price = get_current_price()
    await update.message.reply_text(f"💰 Поточна ціна BTC: {price} USDT")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    news = get_latest_news()
    await update.message.reply_text(f"📰 Останні новини:
{news}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("news", news))
    app.run_polling()
