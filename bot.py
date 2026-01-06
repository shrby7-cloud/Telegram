import requests
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ========= CONFIG =========
TELEGRAM_TOKEN = "7978308856:AAHSiR2fb9PtaEmvmKBsNnSAb-2O-NYMIog"
GROQ_API_KEY = "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"
# ==========================

logging.basicConfig(level=logging.INFO)

def generate_embarrassing_question():
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "system",
                "content": "Generate one awkward but non-sexual embarrassing question in Arabic."
            }
        ],
        "temperature": 0.9
    }

    response = requests.post(url, headers=headers, json=data, timeout=20)
    response.raise_for_status()

    result = response.json()
    return result["choices"][0]["message"]["content"].strip()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبًا 👋\n"
        "أنا بوت الأسئلة المحرجة بالذكاء الاصطناعي 😈\n\n"
        "اكتب /question للحصول على سؤال محرج."
    )

async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("⏳ أفكّر بسؤال محرج...")
        q = generate_embarrassing_question()
        await update.message.reply_text(f"😅 {q}")
    except Exception as e:
        logging.error(e)
        await update.message.reply_text("❌ حدث خطأ في توليد السؤال.")

async def fallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👀 مثير للاهتمام… أكمل.")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("question", question))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fallback))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
