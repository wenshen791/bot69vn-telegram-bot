
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "7545734397:AAHN5Tt4IFUKkAWb8mgIAzueMZXq81Kgmts"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton("🚀 Truy cập 69VN", web_app={"url": "https://69vntrangchu.com"})
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎰 Chào mừng đến với 69VN! Bấm nút bên dưới để mở mini app:",
        reply_markup=reply_markup
    )

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
