from unittest import TestCase
from telebot.model.tables import User, Message


class UserTest(TestCase):
    def setUp(self):
        self.user_id = "1234"
        self.first_name = "Test"
        self.last_name = "User"

        self.test_user = User(
            user_id=self.user_id,
            first_name=self.first_name,
            last_name=self.last_name
        )

    def test_create_user(self):
        self.assertIsInstance(self.test_user, User)


class MessageTest(TestCase):
    def setUp(self):
        self.bot_response = "1234"
        self.user_id = "Test"
        self.user_msg = "User"

        self.test_message = Message(
            bot_response=self.bot_response,
            user_id=self.user_id,
            user_msg=self.user_msg
        )

    def test_create_message_instance(self):
        self.assertIsInstance(self.test_message, Message)
