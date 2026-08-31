import telebot
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_DO_GROQ = os.getenv("MEU_TOKEN_GROQ")
TELEBOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

meu_client = Groq(api_key=TOKEN_DO_GROQ)

my_projetc_bot = telebot.TeleBot(TELEBOT_TOKEN)

meu_client = Groq(api_key=TOKEN_DO_GROQ)

@my_projetc_bot.message_handler(commands= ['Help', 'start'])
def boas_vindas(mensagem):
    my_projetc_bot.reply_to(mensagem, "Olá, sou um bot do telegram de testes\n Estou aqui para te ajudar apenas!")


@my_projetc_bot.message_handler(func = lambda mensagem: True)
def recebendo_mensagem(mensagem):
    
    def chamada_groq():

        chamada = meu_client.chat.completions.create(
            messages = [
                {
                    "role": "user",

                    "content": mensagem.text
                }
            ],
            model= "openai/gpt-oss-20b"
        )

        print(chamada.choices[0].message.content)

        return chamada.choices[0].message.content

    chamada_fun = chamada_groq()

    my_projetc_bot.reply_to(mensagem, chamada_fun)


my_projetc_bot.infinity_polling()