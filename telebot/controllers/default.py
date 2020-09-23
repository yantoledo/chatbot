from telebot import app, TOKEN, bot, db
import telegram
from flask import request
from telebot.functions import msg_to_send
from telebot.model.tables import User, Message


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object

    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    user_msg = update.message.text.encode('utf-8').decode()

    select = User.query.filter_by(user_id=chat_id).all()

    if not select:
        user = User(chat_id, update.message.chat.first_name, update.message.chat.last_name)
        db.session.add(user)

    bot_response = msg_to_send(user_msg)
    message = Message(bot_response, chat_id, user_msg)
    db.session.add(message)

    db.session.commit()

    bot.sendMessage(chat_id=chat_id, text=bot_response)

    return 'ok'


@app.route('/')
def index():
    return '/{}'.format(TOKEN)