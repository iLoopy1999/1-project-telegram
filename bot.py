import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")

keyboard = [["📷   Send Photo"], ["ℹ️   About"]]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! Choose:", reply_markup=markup)

async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "📷   Send Photo":
        with open("test.png", "rb") as photo:
            await update.message.reply_photo(photo)
    elif update.message.text == "ℹ️   About":
        await update.message.reply_text("This bot runs on Render 🌐")
    else:
        await update.message.reply_text("Please pick a valid option.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_msg))

if __name__ == "__main__":
    app.run_polling()

