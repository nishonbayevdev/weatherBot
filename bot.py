import requests
from telegram import message
from telegram.ext import Updater ,CommandHandler,CallbackContext,MessageHandler,Filters
from telegram.update import Update
weatherBot = Updater(token='You should put your token here')
greating = "Assalomu alaykum iltimos manzilingizni yuboring joylashuv bo'limiga kirib"
def hello(update:Update,context:CallbackContext):
    update.message.reply_text(greating)
disp = weatherBot.dispatcher
disp.add_handler(CommandHandler('start',hello))

def location(update:Update,contex:CallbackContext):
    userLocation = update.message.location
    weatherData = requests.get(f'https://api.tomorrow.io/v4/timelines?location=-{userLocation.latitude},{userLocation.longitude}&fields=temperature&timesteps=1h&units=metric&apikey=x7FRGbENHIGTny8uJxLAR0eGoCc64rAd').json()
    tadayWeather = ''
    for i in weatherData['data']['timelines'][0]['intervals']:
        time = i['startTime'][:10]
        temperature = i['values']['temperature']
        tadayWeather += f'vaqti {time} va harorati {temperature}'+'\n'
    update.message.reply_text(tadayWeather)
    print(userLocation.latitude,userLocation.longitude)
disp.add_handler(MessageHandler(Filters.location,location))
weatherBot.start_polling()
weatherBot.idle()
