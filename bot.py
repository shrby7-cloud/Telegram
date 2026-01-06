import requests
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TELEGRAM_TOKEN = "7978308856:AAHSiR2fb9PtaEmvmKBsNnSAb-2O-NYMIog"
GROQ_API_KEY = "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"

def generate_embarrassing_question():
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = (
        "Generate ONE embarrassing but non-sexual question in Arabic. "
        "It should be social or psychological, light but awkward. "
        "Do not include explanations, only the question."
    )

    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You generate awkward but safe questions."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.9
    }

    response = requests.post(url, headers=headers, json=data, timeout=30)
    return response.json()["choices"][0]["message"]["content"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبًا 👋\n"
        "أنا بوت الأسئلة المحرجة بالذكاء الاصطناعي 😈\n\n"
        "اكتب /question لسؤال محرج جديد."
    )

async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        q = generate_embarrassing_question()
        await update.message.reply_text(f"😅 سؤال محرج:\n\n{q}")
    except Exception:
        await update.message.reply_text("حدث خطأ مؤقت، حاول مرة أخرى.")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👀 هه… إجابة مثيرة للاهتمام.")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("question", question))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
