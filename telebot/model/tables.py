from telebot import db


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))

    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<User %r>" % self.user_id


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    user_msg = db.Column(db.Text)
    bot_response = db.Column(db.Text)
    date = db.Column(db.Date)

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, bot_response, user_id, user_msg):
        self.bot_response = bot_response
        self.user_id = user_id
        self.user_msg = user_msg


    def __repr__(self):
        return "<Content %r>" % self.id
