from telebot.functions import validation, operation, msg_to_send


def test_validation_is_zero(app):
    text = "test"
    assert validation(text) is 0


def test_validation_returns_int(app):
    text = "1"
    assert validation(text) is 1


def test_operation_returns_fizz(app):
    number = 3
    assert operation(number) is "Fizz"


def test_operation_returns_buzz(app):
    number = 5
    assert operation(number) is "Buzz"


def test_operation_returns_fizzbuzz(app):
    number = 15
    assert operation(number) is "FizzBuzz"


def test_operation_returns_number(app):
    number = 2
    assert operation(number) == "2"


def test_msg_to_send_start(app):
    text = "/start"
    assert type(msg_to_send(text)) is type(str())


def test_msg_to_send_fizzbuzz(app):
    text = "15"
    assert msg_to_send(text) is "FizzBuzz"


def test_msg_to_send_buzz(app):
    text = "5"
    assert msg_to_send(text) is "Buzz"


def test_msg_to_send_fizz(app):
    text = "3"
    assert msg_to_send(text) is "Fizz"


def test_msg_to_send_number(app):
    text = "asda"
    assert msg_to_send(text) == "Digite um número inteiro!"

