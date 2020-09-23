Instruções para uso do programa:

Versão do Python utilizada: 3.8

Ajustar a variável "app.config['SQLALCHEMY_DATABASE_URI']" localizada em ChatBot/telebot/__init__.py,
onde:

    'mysql+pymysql://(user):(senha do usuário)@localhost/(schema do banco)'

Para realizar a migration no banco local, utilizar o comando:
   >> python run.py db upgrade

O token e o nome de usuário do bot criado estão localizados em ChatBot/telebot/credentials.py

Como eu estava testando localmente?
Faço uma requisição POST para o bot em: "http://127.0.0.1:5000/1132460089:AAFdQzKRx8nqzPiWZZlqx5iwFOkcVxqsifQ"
com o seguinte payload:

{"update_id":732632831,
"message":{
    "message_id":88,
    "from":{
        "id":ID_USUARIO,
        "is_bot":false,
        "first_name":"Yan",
        "last_name":"Toledo",
        "language_code":"pt-br"},
    "chat":{"id":ID_USUARIO,
        "first_name":"Yan",
        "last_name":"Toledo",
        "type":"private"},
    "date":1600556365,
    "text":"2"
        }

IMPORTANTE!!
Adequar o valor de ID_USUARIO para o usuário que estiver em contato com o bot pelo telegram.

O bot recebe a requisição e responde para o usuário no telegram.