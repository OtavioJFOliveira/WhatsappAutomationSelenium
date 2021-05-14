
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

time.sleep(25)

contatos = ['Amor','Whelo']

mensagem = "mensagem de teste"

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element_by_xpath('//div[contains(@data-tab,"6")]')
    campo_mensagem.click()
    time.sleep(3)
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)