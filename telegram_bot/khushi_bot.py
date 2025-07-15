from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace this with your real bot token
TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

# /start command handler
def start(update, context):
    update.message.reply_text("Assalamualaikum, I’m Khushi’s bot!")

# Text message handler
def reply(update, context):
    msg = update.message.text.lower()

    if "hello" in msg:
        update.message.reply_text("Hi! How can I help you?")
    elif "who are you" in msg:
        update.message.reply_text("I'm Khushi’s personal bot.")
    elif "how are you" in msg:
        update.message.reply_text("I'm doing great, Alhamdulillah!")
    elif "bye" in msg:
        update.message.reply_text("Allah Hafiz!")
    elif "khushi" in msg:
        update.message.reply_text("That's me! 🌸")
    else:
        update.message.reply_text("Sorry, I didn’t understand that.")

# Main function to set up the bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    updater.start_polling()
    updater.idle()

# This ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
