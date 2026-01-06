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
TELEGRAM_TOKEN = "7978308856:AAHAGP78WOsH2z-3i0wnAqjVm7pW9-J93v4"
GROQ_API_KEY = "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"

logging.basicConfig(level=logging.INFO)

def generate_embarrassing_question():
    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "user",
                    "content": "اكتب سؤالًا واحدًا محرجًا اجتماعيًا أو نفسيًا بدون أي محتوى جنسي."
                }
            ],
            "temperature": 0.9,
            "max_tokens": 80
        },
        timeout=30
    )

    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"].strip()

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
    await update.message.reply_text("👀 مثير للاهتمام…")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("question", question))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fallback))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
