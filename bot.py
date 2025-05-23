import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Menu de langues
LANGUAGES = {
    "Français": "Bienvenue sur Crypto Opportunités!",
    "English": "Welcome to Crypto Opportunities!",
    "Español": "¡Bienvenido a Crypto Opportunidades!",
    "العربية": "مرحبًا بك في فرص العملات الرقمية!"
}

# Démarrer le bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[lang] for lang in LANGUAGES.keys()]
    await update.message.reply_text(
        "Choisissez votre langue / Choose your language / Elige tu idioma / اختر لغتك",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )

# Réponse selon langue
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_lang = update.message.text
    if user_lang in LANGUAGES:
        await update.message.reply_text(LANGUAGES[user_lang])
    else:
        await update.message.reply_text("Commande non reconnue.")

def main():
    import dotenv
    dotenv.load_dotenv()
    token = os.getenv("BOT_TOKEN")
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()