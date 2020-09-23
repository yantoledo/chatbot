def validation(text):
    if text.isdigit():
        return int(text)
    else:
        return 0


def operation(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


def msg_to_send(text):
    if text == "/start":
        # print the welcoming message
        return "Digite um número inteiro!"
    elif validation(text) != 0:
        number = validation(text)
        return operation(number)
    else:
        return "Digite um número inteiro!"
