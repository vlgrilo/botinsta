import time
import random
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InstagramBot:
    def __init__(self, username, password, link):
        self.username = username
        self.password = password
        self.link = link
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile=firefoxProfile, executable_path=r"./geckodriver")

    def login(self): 
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        time.sleep(3)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(5)
        bot.comenta(0)

    @staticmethod
    def humano(palavra, campo):
        for letter in palavra:
            campo.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def comenta(self, cont):
        driver = self.driver
        driver.get(self.link)
        print(datetime.datetime.now()) 
        qtd = random.randint(40, 60)
        print('Sera feito', qtd, 'comentarios')
        for x in range(qtd):
            try:
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                campo_comentario.clear()
                self.humano(random.choice(comentario), campo_comentario)
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                cont += 1
                time.sleep(random.randint(30,60))
            except Exception as e:
                print(e)
                cont -= 1
                print(datetime.datetime.now())
                tempo = random.randint(3600, 5400)
                print('Comentarios fetios:', cont, 'Tempo parado:', tempo/60, 'minutos')             
                time.sleep(tempo)
                bot.comenta(cont)
        tempo = random.randint(3600, 5400)
        print(datetime.datetime.now()) 
        print('Comentarios fetios:', cont, 'Tempo parado:', tempo/60, 'minutos')
        time.sleep(tempo)
        bot.comenta(cont)

bot = InstagramBot('LOGIN', 'SENHA', 'LINK DA FOTO')

comentario = ('@USUARIO', '@USUARIO', '@USUARIO')

#comentario = ('💖', '💖💖', '💖💖💖', '💕', '💕💕', '💕💕💕', '🖤', '🖤🖤', '🖤🖤🖤', '💜', '💜💜', '💜💜💜', '💛', '💛💛', '💛💛💛')

bot.login()