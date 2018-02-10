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
    bot.send_message(message.chat.id, "Olá, do que você precisa hoje?")

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

@bot.message_handler(func=lambda message: True, content_types=['audio'])
def command_default(message):
    bot.send_message(message.chat.id, "Eu sou um programa brother, cê acha que eu vou ficar ouindo áudio? Facilita minha vida, só me manda o tipo do arquivo (.xxxx)")

# Responde uma pergunta

@bot.message_handler(func=is_pergunta)
def responde_pergunta(message):
    bot.reply_to(message, "Sei lá cara, pergunta no posto ipiranga")


####################################3


##### Tipos de arquivos ###########

''' Exemplo '''
@bot.message_handler(func=lambda msg: msg.text == ".xxx")
def arquivo_xxx(msg):
    bot.reply_to(msg, "")


''' TXT '''
@bot.message_handler(func=lambda msg: msg.text == ".txt")
def arquivo_txt(msg):
    bot.reply_to(msg, "O TXT é um arquivo texto ou texto puro como é mais conhecido. Ele é um formato que indica um texto sem formatação, podendo ser aberto ou criado no Bloco de Notas do Windows, por exemplo.")


''' EXE '''
@bot.message_handler(func=lambda msg: msg.text == ".exe")
def arquivo_exe(msg):
    bot.reply_to(msg, "EXE é um tipo de arquivo usado no Windows para designar um aplicativo ou um programa executável. Ele pode ser o programa responsável pela instalação de um software, como pode ser o aplicativo principal do próprio software.")


''' DLL '''
@bot.message_handler(func=lambda msg: msg.text == ".dll")
def arquivo_dll(msg):
    bot.reply_to(msg, "Também conhecida como biblioteca de vínculo dinâmico, é um arquivo que é usada geralmente junto como EXE como parte complementar de um software.")


''' ZIP '''
@bot.message_handler(func=lambda msg: msg.text == ".zip")
def arquivo_zip(msg):
    bot.reply_to(msg, "Indica um arquivo compactado com outros arquivos ou pastas. É muito usado quando necessitamos enviar para outros locais uma grande quantidade de conteúdo ou pastas, então para diminuir o tamanho e facilitar o processo usa-se a compactação. O RAR é outro formato compactado bastante conhecido também. Para extrair os arquivos compactados basta usar programas como WinRAR e 7zip")

###################################

# Qualquer outra coisa que a pessoa falar
@bot.message_handler(func=lambda message: True, content_types=['text'])
def responde_outras_coisas(message):
    bot.send_message(message.chat.id, "Não entendi cara")

# Iniciando o bot
bot.polling()

