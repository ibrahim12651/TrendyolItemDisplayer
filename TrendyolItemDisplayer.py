


import selenium
import pyautogui
from time import sleep
from selenium import webdriver
from os import system, name
from discord_webhook import DiscordWebhook , DiscordEmbed
from progress.bar import IncrementalBar


esya = input("İsteğinizi Eşyayı yazınız.: ")


with IncrementalBar('Yükleniyor..', max=5000) as bar:
    for i in range(5000):
        
        bar.next() 


driver = webdriver.Chrome()
url = "https://www.trendyol.com/butik/liste/2/erkek"
driver.get(url)
sleep(5)

driver.maximize_window()

sleep(5)
arama = driver.find_element_by_class_name("search-box").click()

yaz = driver.find_element_by_class_name("search-box").send_keys(esya)

sleep(2)

ara = driver.find_element_by_class_name("search-icon").click()
sleep(9)

try:
    perde = driver.find_element_by_class_name("overlay").click()
    sleep(2)
except:
  print("Birşeyler ters gitti.")
finally:
    telefon = driver.find_element_by_xpath('//*[@id="search-app"]/div/div[1]/div[2]/div[4]/div/div[2]/div[1]/a/div[2]/div[1]/div/span[2]').text
    sleep(2)
    tikla = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div[2]/div[1]').click()
    sleep(2)




sleep(3)

fiyat = driver.find_element_by_class_name("prc-box-dscntd").text



clear = lambda: system("clear" if name == "posix" else "cls")
clear()

print(fiyat)

sleep(2)
driver.switch_to.window(driver.window_handles[1])

driver.save_screenshot("telefon.png")
sleep(2)

webhook = DiscordWebhook(url='')

with open("telefon.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='example.png')
    embed = DiscordEmbed(title=telefon,color='03b2f8')
    embed.add_embed_field(name='Fiyat', value=driver.find_element_by_class_name("prc-box-dscntd").text)
    webhook.add_embed(embed)
    response = webhook.execute()
  #  sleep(30)
   # webhook.delete(response)
    sleep(30)
    driver.close()
    driver.quit()
