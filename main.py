import requests, time
#identificador grupo telegram: 
#identificador grupo: -4154419863
#token bot: 6870057041:AAHKI5EbdpaadPtEs1PqfLgo0t64toS4s5c
#nombre: MarcCB Bot

#token bot 2: 6317835179:AAGgKkFiybtTbD20OUuXpTjtQ3spkIJw_Y0
#nombre: Marc CB Bot2

bots = []
class Bot:
    def __init__(self, token, name):
        self.name = name
        self.api = 'https://api.telegram.org/bot'
        self.token = token
        self.chat_id = '-4154419863'
        self.method = ''
        self.text = ''
        self.url = ''
        self.messages = []

    def setUrl(self):
        self.url = f"{self.api}{self.token}{self.method}"
        

    def SendMessage(self):
        self.method = '/sendMessage'
        self.text = 'Hola! Esto es un mensaje de prueba'
        self.url = self.api + self.token + self.method + '?chat_id=' + self.chat_id + '&text=' + self.text
        response = requests.get(self.url)
        self.messages.append(response.json()['result']['message_id'])

    
    def SendPhoto(self):
        self.method = '/sendPhoto'
        self.setUrl()
        with open("./memes-humor-redes_sociales_178744040_23538138_1706x960.webp", 'rb') as photo:
            response = requests.post(self.url,data={'chat_id':self.chat_id}, files={'photo': photo})
            print(response.text)

    def SendDocument(self):
        self.method = '/sendDocument'
        with open('./hola.txt', 'rb') as doc:
            params = {'chat_id': self.chat_id}
            files = {'document': doc}
            self.setUrl()
            response = requests.post(self.url, params=params, files=files)

    def DeleteMessage(self):
        self.method = '/deleteMessage'
        last_message = self.messages[-1]
        self.messages.pop()
        params = {'chat_id': self.chat_id, 'message_id': last_message}
        self.setUrl()
        requests.post(self.url,params=params)

    def EditMessage(self):
        self.method = '/editMessageText'
        last_message = self.messages[-1]
        params = {'chat_id': self.chat_id, 'message_id': last_message, 'text': 'Este es el texto editado'}
        self.setUrl()
        requests.post(self.url,params=params)


bot1 = ('6870057041:AAHKI5EbdpaadPtEs1PqfLgo0t64toS4s5c', 'MarcCB Bot')
bot2 = ('6317835179:AAGgKkFiybtTbD20OUuXpTjtQ3spkIJw_Y0', 'Marc CB Bot 2')