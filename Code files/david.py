import telebot

bot = telebot.TeleBot('440679971:AAFCLsXigp-xzUw-aHsuzzjp9RuZkxIAnlc')


###### Respondendo coisas básicas ########


# Comando Start Ou Help
@bot.message_handler(commands=['start','help'])

def show_help(message):
    bot.reply_to(message, 
            "E ai cara, estou aqui para te ajudar a conhecer todos os tipos de arquivos \n Se você não reconheceu a extensão de um arquivo e quer saber mais, é só me mandar!\n\n Ex: .py .dat .exe \n\n" +
            "/start - Inicia o bot (se você está lendo isso, você já iniciou, relaxa)\n" +
            "/help - Mostra a ajuda (É isso que você ta lendo)\n" +
            "\n Por enquanto só tenho esses comandos, estou em desenvolvimento ainda \n" +
            "\n Última atualização - 01/2018 ")


# Responde "oi"
@bot.message_handler(func=lambda message: message.text == "Oi")
def responde_oi(message):
    bot.send_message(message.chat.id, "Fala mano, do que você precisa hoje?")

    
# Responde "E ai David"
@bot.message_handler(func=lambda message: message.text == "E ai David")
def responde_eai(message):
    bot.send_message(message.chat.id, "Fala brother")

    
# Verifica se é uma pergunta
def is_pergunta(message):
    for c in message.text:
        if c == "?":
            return True
    return False


# Responde um áudio
# @bot.message_handler(func=lambda message: True, content_types=['audio'])
# def command_default(message):
#     bot.send_message(message.chat.id, "Eu sou um programa brother, cê acha que eu vou ficar ouindo áudio? Facilita minha vida, só me manda o tipo do arquivo (.xxxx)")


# Responde uma pergunta
@bot.message_handler(func=is_pergunta)
def responde_pergunta(message):
    bot.reply_to(message, "Sei lá cara, eu só sei reconhecer tipos de arquivos hehe")

    
####################################


######## Tipos de arquivos #########

@bot.message_handler(func=lambda msg: msg.text == ".txt")
def arquivo_txt(msg):
    bot.reply_to(msg, "O TXT é um arquivo texto ou texto puro como é mais conhecido. Ele é um formato que indica um texto sem formatação, podendo ser aberto ou criado no Bloco de Notas do Windows, por exemplo.")

    
####################################


# Qualquer outra coisa que a pessoa falar
@bot.message_handler(func=lambda message: True, content_types=['text'])
def responde_outras_coisas(message):
    bot.send_message(message.chat.id, "Não entendi o que você falou")

# Iniciando o bot
bot.polling()

