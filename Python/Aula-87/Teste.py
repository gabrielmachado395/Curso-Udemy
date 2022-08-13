from selenium import webdriver
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.mensagem = 'Tarde'
        self.grupos = ['Dark Glass']
        self.driver_path = r'C:\Users\gabriel\PycharmProjects\Python-Udemy\Python\Aula-87\chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r'user-data-dir=C:\Users\gabriel\AppData\Local\Google\Chrome\User Data\Default')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )
    def EnviarMensagens(self):
        # <span dir="auto" title="Dark Glass" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">Dark Glass</span>
        # <div class="_2lMWa"><div tabindex="-1">
        # <span data-testid="send" data-icon="send" class="">
        self.chrome.get('https://web.whatsapp.com')
        
        sleep(30)

        grupo = self.chrome.find_element_by_xpath("//span[@title='Dark Glass']")
        grupo.click()
        
        sleep(3)
        
        chat = self.chrome.find_element_by_class_name('p3_M1')
        chat.click()
        
        sleep(3)

        chat.send_keys(self.mensagem)
        
        sleep(3)
        
        enviar = self.chrome.find_element_by_xpath("//span[@data-icon='send']")
        enviar.click()
        
        sleep(3)

bot = ChromeAuto()
bot.EnviarMensagens()