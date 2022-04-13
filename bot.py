
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


#Command Handlers

def hello(update, context):
    update.message.reply_text("Hey what's up guys!")

#function to respond to help cmd
def help(update, context):
    update.message.reply_photo('https://townsquare.media/site/40/files/2015/10/10397010_801652926551438_6207627618968753405_o.jpg?w=1200&h=0&zc=1&s=0&a=t&q=89')

#function to echo the users message
def echo(update, context):
    update.message.reply_text(update.message.text + '🤪')

def hangout(update, context):
    update.message.reply_text("Lets go to the beach!")

def food(update, context):
    update.message.reply_text("Let's get some pizza!")

#function to log errors and display
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)






def main():
    updater = Updater("5202815600:AAE91yiAEArX-5hAEzNjG1DQptdKjz1-UiQ", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("hello", hello))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("food", food))  
    dp.add_handler(CommandHandler("hangout", hangout))
    dp.add_handler(CommandHandler("echo", echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()