from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, filters, Application, ContextTypes
from bot.genai_analyzer import analyze_dream_gemini

TOKEN = "7952203435:AAE2MHE9-MB0zIXAFI3_ojyUD8G1XC4MvIY" 

bot = Bot(token=TOKEN)
application = Application.builder().token(TOKEN).build()

def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text("Hello Welcome!! 💭 Is there any Dream to Discuss? (Yes/No)")

def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    user_data = context.user_data

    if text == "yes":
        update.message.reply_text("Tell me about your dream 💭")
        user_data["waiting_for_dream"] = True
    elif text == "no":
        update.message.reply_text("No problem 😴💤! We can discuss later.")
    elif user_data.get("waiting_for_dream"):
        user_data["dream_text"] = text
        update.message.reply_text("Would you like to finish the story or analyze your dream? (story/analysis)")
        user_data["waiting_for_dream"] = False
        user_data["waiting_for_choice"] = True
    elif user_data.get("waiting_for_choice"):
        mode = text
        dream = user_data.get("dream_text", "")
        if mode in ["story", "analysis"]:
            result = analyze_dream_gemini(dream, mode)
            update.message.reply_text(result)
            update.message.reply_text("Want to share more dreams? (Yes/No)")
        else:
            update.message.reply_text("Invalid choice. Please enter 'story' or 'analysis'.")
        user_data.clear()
    else:
        update.message.reply_text("I'm not sure what you mean 🤔. Please reply with Yes or No.")

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    print("Bot is running...")
    application.run_polling()
