import selenium
from time import sleep
from selenium import webdriver
from os import system, name
from discord_webhook import DiscordWebhook , DiscordEmbed
from progress.bar import IncrementalBar
from selenium.webdriver.common.by import By


esya = input("İsteğinizi Eşyayı yazınız : ")


with IncrementalBar('Yükleniyor..', max=5000) as bar:
    for i in range(5000):
        bar.next()
bar.finish()

       



driver = webdriver.Chrome()
url = "https://www.trendyol.com/butik/liste/2/erkek"
driver.get(url)
sleep(5)

driver.maximize_window()

sleep(5)
arama = driver.find_element(By.CLASS_NAME,'search-box').click()

yaz = driver.find_element(By.CLASS_NAME,'search-box').send_keys(esya)

sleep(2)
ara = driver.find_element(By.CLASS_NAME,'search-icon').click()
sleep(9)

try:
    perde = driver.find_element(By.CLASS_NAME,'overlay').click()
    sleep(2)
except:
  print("Birşeyler ters gitti.")
finally:
    telefon = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div/div/div/div[1]/div[2]/div[4]/div[1]/div/div[2]/div[1]/a/div[2]/div[1]/div/div').text
    sleep(2)
    tikla = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div/div/div/div[1]/div[2]/div[4]/div[1]/div/div[2]/div[1]').click()
    sleep(2)

sleep(3)

fiyat = driver.find_element(By.CLASS_NAME,"prc-box-dscntd").text

clear = lambda: system("clear" if name == "posix" else "cls")
clear()

print(fiyat)

sleep(2)
driver.switch_to.window(driver.window_handles[1])

driver.save_screenshot("telefon.png")
sleep(2)

webhook = DiscordWebhook(url='') #Webhook url gelicek

with open("telefon.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='telefon.png')
    embed = DiscordEmbed(title=telefon,color='03b2f8')
    embed.add_embed_field(name='Fiyat', value=fiyat)
    webhook.add_embed(embed)
    response = webhook.execute()
    sleep(30)    
    clear = lambda: system("clear" if name == "posix" else "cls")
    clear()
    print(telefon)
    print(fiyat)
    print("Başarılı")
    sleep(2)
    driver.close()
    driver.quit()
