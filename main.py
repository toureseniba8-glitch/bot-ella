import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from google import genai

# Récupération des clés d'accès
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

ai_client = genai.Client(api_key=GEMINI_KEY)

async def repondre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_utilisateur = update.message.text
    
    # Génération de la réponse par Gemini
    reponse = ai_client.models.generate_content(
        model='gemini-2.5-flash',
        contents=message_utilisateur,
    )
    await update.message.reply_text(reponse.text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, repondre))
    app.run_polling()
