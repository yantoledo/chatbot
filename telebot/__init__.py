from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import telegram
from telebot.credentials import bot_token, bot_user_name

global bot
global TOKEN

TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)


def create_app():
    return Flask(__name__)


app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://yan:123456@localhost/chatbot'
db = SQLAlchemy(app)


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


from telebot.controllers import default