from config import TOKEN
from morfology import analysis
from transcription import transcription
from quiz import poll


import telebot
from telebot import types

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
     
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Транскрипция!')
    but2 = types.KeyboardButton('Морфемы!')
    but3 = types.KeyboardButton('Квиз по фонетике!')
    markup.add(but1, but2, but3)

    bot.send_message(message.chat.id, "Опять работа...", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def reply(message):
    if message.text == 'Транскрипция!':
        bot.send_message(message.chat.id, 'Отправьте слово для транскрипции. Все буквы, кроме ударной гласной должны быть строчными')
        bot.register_next_step_handler(message, bot_transcription)

    elif message.text == 'Морфемы!':
        bot.send_message(message.chat.id, 'Отправьте слово для разбора. Будет разобрана его начальная форма!')
        bot.register_next_step_handler(message, bot_analisys)

    elif message.text == 'Квиз по фонетике!':
        bot_poll(message)



def bot_analisys(message):
    if message.text == 'Транскрипция!':
        bot.register_next_step_handler(message, bot_transcription)
        return
    if message.text == 'Квиз по фонетике!':
        bot.register_next_step_handler(message, bot_poll)
        return
    
    try:
        bot.send_message(message.chat.id, analysis(message.text), reply_to_message_id=message.message_id)
        bot.register_next_step_handler(message, bot_analisys)
    except:
        bot.send_message(message.chat.id, "Что-то пошло не так.\nНе делайте так больше...")
        bot.register_next_step_handler(message, bot_analisys)



def bot_transcription(message):
    if message.text == 'Морфемы!':
        bot.register_next_step_handler(message, bot_analisys)
        return
    if message.text == 'Квиз по фонетике!':
        bot.register_next_step_handler(message, bot_poll)
        return
    
    try:
        bot.send_message(message.chat.id, transcription(message.text), reply_to_message_id=message.message_id)
        bot.register_next_step_handler(message, bot_transcription)
    except:
        bot.send_message(message.chat.id, "Что-то пошло не так, возможно неправильно выделено ударение.\nНе делайте так больше...")
        bot.register_next_step_handler(message, bot_transcription)
   

def bot_poll(message):
    pollinfo = ("Это квиз по фонетике! Будет 10 вопросов.\nЧтобы успешно пройти его, вы можете ознакомиться с предложенными материалами:\n"
                + "https://nauka.club/wp-content/auploads/855172/klassifikaciya_soglasnyh.jpg" + '\n' +
                "https://rus-et.ru/wp-content/uploads/2020/08/glasnye-russkogo-yazyka.jpg" + '\n' + 
                "И оцените это! https://imaginary.github.io/pink-trombone/") 
    bot.send_message(message.chat.id, pollinfo, disable_web_page_preview=True)
    global number, score
    score = 0
    number = 10
    global res, correct_option_id
    options, correct_option_id, question = poll()
    bot.send_poll(message.chat.id, question=question, options=options, correct_option_id=correct_option_id , type='quiz', is_anonymous=False)
        
@bot.poll_answer_handler()
def poll_answer(pol):
    global number, res, correct_option_id, score
    number -= 1
    if pol.option_ids[0] == correct_option_id:
        score += 1
    if number > 0:
        options, correct_option_id, question = poll()
        bot.send_poll(pol.user.id, question=question, options=options, correct_option_id=correct_option_id , type='quiz', is_anonymous=False)
    
    if number == 0:
        bot.send_message(pol.user.id, f"Ваш результат {score} из 10")



bot.infinity_polling()