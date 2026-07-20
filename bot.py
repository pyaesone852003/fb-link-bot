from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    lines = [line.strip() for line in user_text.split('\n') if line.strip()]
    
    if not lines:
        await update.message.reply_text("ကျေးဇူးပြု၍ လင့်ခ်များကို တစ်ကြောင်းချင်းစီ ပို့ပေးပါ။")
        return

    result_text = ""
    for index, link in enumerate(lines, start=1):
        result_text += f"{index}. {link}\n"

    await update.message.reply_text(result_text.strip())

if __name__ == '__main__':
    TOKEN = "8974543534:AAE9hi57XOsImdvwI4gA9VUR5QDjGlDLpOk"
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Bot စတင်အလုပ်လုပ်နေပါပြီ...")
    app.run_polling()
