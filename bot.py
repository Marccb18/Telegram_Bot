import requests
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
        bots.append(self)

    def setUrl(self):
        self.url = f"{self.api}{self.token}{self.method}"

    def saveMessage(self,response):
        self.messages.append(response.json()['result']['message_id'])

        
    def SendMessage(self, text):
        self.method = '/sendMessage'
        self.text = text
        self.url = self.api + self.token + self.method + '?chat_id=' + self.chat_id + '&text=' + self.text
        response = requests.get(self.url)
        self.saveMessage(response)

    
    def SendPhoto(self):
        self.method = '/sendPhoto'
        self.setUrl()
        with open("./memes-humor-redes_sociales_178744040_23538138_1706x960.webp", 'rb') as photo:
            response = requests.post(self.url,data={'chat_id':self.chat_id}, files={'photo': photo})
            self.saveMessage(response)

    def SendDocument(self):
        self.method = '/sendDocument'
        with open('./hola.txt', 'rb') as doc:
            params = {'chat_id': self.chat_id}
            files = {'document': doc}
            self.setUrl()
            response = requests.post(self.url, params=params, files=files)
            self.saveMessage(response)

    def DeleteMessage(self):
        self.method = '/deleteMessage'
        try:
            last_message = self.messages[-1]
        except:
            return print('No hay mensajes para eliminar')
        self.messages.pop()
        params = {'chat_id': self.chat_id, 'message_id': last_message}
        self.setUrl()
        requests.post(self.url,params=params)

    def EditMessage(self, text):
        if self.method != '/sendMessage':
            return print('No se puede editar un mensaje que no sea un texto')
        self.method = '/editMessageText'
        last_message = self.messages[-1]
        params = {'chat_id': self.chat_id, 'message_id': last_message, 'text': text}
        self.setUrl()
        requests.post(self.url,params=params)