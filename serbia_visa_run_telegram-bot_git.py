import telebot
from datetime import date, datetime, timedelta

#create bot
bot = telebot.TeleBot ("Bot API here")

#process "/start" command
@bot.message_handler (commands=['start'])
def start (m):
    bot.send_message(m.chat.id,"Please add date of your arrival to Serbia in dd.MM.YYYY format \n")

#receive imput from user
@bot.message_handler (content_types=["text"])
def handle_text (message):
    try:
        e_date_string = message.text
        e_datetime = datetime.strptime(e_date_string, "%d.%m.%Y")
    except:
        bot.send_message(message.chat.id, "Date format is invalid. Please try again.")
        
    else:        
        e_date = e_datetime.date ()
        c_date = date.today()

        delta = c_date - e_date
        days_of_stay = delta.days
        d_date = e_date + timedelta (days=30)
        s_depart = d_date - timedelta (days=4)

        bot.send_message(message.chat.id, f"It is day {days_of_stay} of stay")
        bot.send_message(message.chat.id, f"Last day to depart is {d_date.strftime('%d.%m.%Y')}")
        bot.send_message(message.chat.id, f"It's safe to depart around {s_depart.strftime('%d.%m.%Y')}")


#run bot
bot.polling(none_stop=True, interval=0)
