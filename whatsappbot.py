#Importando Bibliotecas | Importing Libraries
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.common.keys import Keys

#Abrindo o Whatsapp | Opening Whatsapp
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
time.sleep(10)

#Criando as funções | Creating Functions
def search_contacts(contact):
    search = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    search.click()
    search.send_keys(contact)
    search.send_keys(Keys.ENTER)

def send_msg(msg):
    send = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    send[1].click()
    send[1].send_keys(msg)
    send[1].send_keys(Keys.ENTER)

#Definindo os Contatos e/ou Grupos | Defining Contacts and/or Groups
contacts = ['Letícia Soto', 'Júlio']
msg = ['Enviando msg pelo python 1', 'Enviando msg pelo python 2']

#Procurando os Contatos e/ou Grupos e enviando mensagem | Searching Contacts and/or Groups and sending message
for contatc, msg in zip(contacts, msg):
    search_contacts(contatc)
    send_msg(msg)