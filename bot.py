from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import requests

TELEGRAM_TOKEN = "7978308856:AAHSiR2fb9PtaEmvmKBsNnSAb-2O-NYMIog"

import random
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = "7978308856:AAHSiR2fb9PtaEmvmKBsNnSAb-2O-NYMIog"

EMBARRASSING_QUESTIONS = [
    "ما أكثر موقف شعرت فيه بالإحراج ولم تنسه إلى الآن؟",
    "هل سبق أن أرسلت رسالة لشخص بالخطأ وندمت فورًا؟",
    "ما عادة لديك تعرف أنها غريبة لكنك ما زلت تفعلها؟",
    "هل سبق أن تظاهرت بفهم شيء وأنت لا تفهمه أبدًا؟",
    "ما أسوأ اسم حفظت به شخصًا في هاتفك؟",
    "هل سبق أن ضحكت في موقف كان يجب أن تكون فيه جادًا؟",
    "ما أطول مدة تجاهلت فيها رسالة متعمدًا؟",
    "هل سبق أن نسيت اسم شخص بعد ثوانٍ من التعارف؟",
    "ما أكثر كذبة اجتماعية تقولها كثيرًا؟",
    "هل سبق أن دخلت مكانًا ثم نسيت لماذا دخلت؟"
]

COMMENTS = [
    "هممم… هذا جواب مثير للاهتمام 😅",
    "واضح أنك فكرت كثيرًا قبل الرد.",
    "هذا النوع من الإجابات لا يُقال بسهولة.",
    "أحاول ألا أحكم… لكن الوضع محرج فعلًا.",
    "سأحتفظ بهذه المعلومة في ذاكرتي الافتراضية.",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبًا 👋\n"
        "أنا بوت الأسئلة المحرجة 😈\n\n"
        "اكتب /question للحصول على سؤال محرج."
    )

async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = random.choice(EMBARRASSING_QUESTIONS)
    await update.message.reply_text(f"سؤال محرج:\n\n{q}")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    comment = random.choice(COMMENTS)
    await update.message.reply_text(comment)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("question", question))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
