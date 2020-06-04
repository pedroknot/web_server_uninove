import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.buscape.com.br')

try:
    driver.find_element_by_xpath('//*[@id="home-heading"]/div/div/div[2]/div/input').click()
    busca = driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/form/div[1]/div/input')
except:
    busca = driver.find_element_by_xpath('//*[@id="header"]/div/div/div[3]/div/div[1]/input')
busca.click()
busca.send_keys("iphone 11")
busca.send_keys(Keys.ENTER)


# for i in range(3):
time.sleep(2)
ver_precos = driver.find_element_by_xpath(f'//*[@id="pageSearchResultsBody"]/div[2]/div[1]/div[2]/div[3]/a')

ver_precos.click()

nome_iphone = driver.find_element_by_xpath('//*[@id="productInfo"]/h1/span').text
print(nome_iphone)
dados_iphone = driver.find_element_by_xpath('/html/body/div[1]/div/section/div[1]/div/ul/li[1]/div[2]').text.replace('Ver detalhes','').replace('Ir à loja','')
link = driver.find_element_by_xpath('/html/body/div[1]/div/section/div[1]/div/ul/li[1]/div[2]/div[3]/a')
print(link.get_attribute('href'))
print(dados_iphone)


driver.close()



