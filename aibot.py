from telegram import *
from telegram.ext import *
from telegram.ext.Updater import Updater 
from telegram.update import Update 
from telegram.ext.callbackcontext import CallbackContext 
from telegram.ext.commandhandler import CommandHandler 
from telegram.ext.messagehandler import MessageHandler 
from telegram.ext.filters import Filters 


Token = ("ur bot id")
updater = Updater("ur bot id", use_context=True)

def start(update, context):
    update.message.reply_text("Hello! Welcome to Greey")
    
def help(update,context):
    update.message.reply_text("""
    The following commands are avilable:
    
    /start -> Welcome to the channel
    /help -> This message
    /content -> Greey CALM's you Down
    /Python  -> python tutorial
    /SQL -> SQL tutorial
    /Java -> Java tutorial
    /Greey -> AIBOT for you
    /contact -> CALL my Owner riyo
     """)
    
def content(update, context):
    update.message.reply_text("We have various playlists and articles available!")

def Python(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/ERCMXc8x7mc?si=_dHY_DDRwDCggXIq")

def SQL(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/hlGoQC332VM?si=8SnJzwWltAgXryuQ")
    
def Java(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/UmnCZ7-9yDY?si=jq18Ma33ZSr16L1T")
    
def Greey(update, context):
    update.message.reply_text("tutorial link : https://github.com/riyanshgandhi")
    
def contact(update, context):
    update.message.reply_text("You can contact on my linkedin")

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")



#print(bot.get_me())

dispatcher = updater.dispatcher

disp.add_handler(CommandHandler('start',start))
disp.add_handler(CommandHandler('help',help))
disp.add_handler(CommandHandler('content',content))
disp.add_handler(CommandHandler('Python',Python))
disp.add_handler(CommandHandler('SQL',SQL))
disp.add_handler(CommandHandler('Java',Java))
disp.add_handler(CommandHandler('Greey',Greey))
disp.add_handler(CommandHandler('contact',contact))
disp.add_handler(MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()