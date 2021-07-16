from weather import get_weather
from TOKEN import TOKEN
from telegram import Update, ForceReply, update
from telegram.ext import Updater, CommandHandler, CallbackContext


def weather(update: Update, context: CallbackContext) -> None:
    data = get_weather()
    city = data['city']
    temp = data['temp']
    country = data['country']

    message = f'En {city}, {country} hay un clima de {temp}C'
    print("respuesta", message)

    update.message.reply_text(message)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("clima", weather))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()