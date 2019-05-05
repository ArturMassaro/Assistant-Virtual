from Bot.ConversationBot import botConversation as bc
from Bot.TextToSpeechBot import TextToSpeech as ts

while(1):

    textUser = input("input: ")

    if(textUser == "sair"):
        ts.convert("ok, até mais")
        exit()

    resposta = bc.Conversation(textUser)
    print(resposta[0])
    ts.convert(resposta[0])

    
