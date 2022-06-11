# Esya_Fiyati_Gosterimi
Telefon Markalarından istediğinizi yazıp size ismini ve fiyatını bir de fotosunu atacaktır.



![image](https://user-images.githubusercontent.com/39805679/173198149-5a9b9636-8e2f-4f91-83f0-6586fe076b6f.png)

Bu modülleri indirmeniz gereklidir yoksa çalışmaz!

pip install selenium <br>
pip install pyautogui <br>
pip install discord-webhook <br>
pip install progress <br>

time ve os modülleri python da kendiliğin de vardır.


## Discord'da WebHook açma

1- Discord sunucusun da sunucu ayarlarına girin <br>
![image](https://user-images.githubusercontent.com/39805679/173200924-1fb968a5-2150-4cd7-9a67-7747eafc2fed.png) <br>
2-  Entegrasyonlar'a tıklayın <br>
![image](https://user-images.githubusercontent.com/39805679/173200936-1f9b4e88-e342-4a6f-8670-c65190a37495.png) <br>
3- Webhook oluştur yazısına tıklayın <br>
![image](https://user-images.githubusercontent.com/39805679/173201040-d2386cf3-4870-40ed-841e-3bb0e5e7f793.png)<br>
4- 3. Madde'yi yaptıktan sonra Açtığınız Webhook'u ismini ve istediğiniz kanalı seçip ayarlayın <br>
![image](https://user-images.githubusercontent.com/39805679/173201337-c27e4052-5f76-4b57-aef8-e8bb9f560521.png) <br>
5- Webhook Url'sini Kopyala yazısına tıklayın <br>
![image](https://user-images.githubusercontent.com/39805679/173201585-8548e0cc-fff6-4157-8f15-a16dba8c85ba.png)<br>
6- webhook = DiscordWebhook(url='') çift tırnağın içine kopyaladığınız linki içine yapıştırın  <br>
![image](https://user-images.githubusercontent.com/39805679/173201734-67a3279c-a7e4-47d2-8b05-5e6a6ea8e075.png) <br>
![image](https://user-images.githubusercontent.com/39805679/173201875-0c10d3a5-de65-4ef9-bdde-e0882d65397a.png) <br>



## Google Sürümü Kontrol Etme Ve Güncelleme

1- Google açın 3 noktalıya tıklayıp ayarlara tıklayın <br>
2- Chrome hakkındaya tıklayın <br>
![image](https://user-images.githubusercontent.com/39805679/173199033-a7417c5c-6b4e-44b8-9e9f-d652287d471e.png) <br>
3- Chrome hakkındaya tıkladıktan sonra  sürümü gösterilir <br>
![image](https://user-images.githubusercontent.com/39805679/173199204-a7c6bafb-b664-4112-a305-ddb149820309.png) <br>
4- [ChromeDriver](https://chromedriver.chromium.org/downloads) – Verdiğim linke tıklayıp chromedriver sitesine gidersiniz oradan size uygun sürümü bulup indirin <br>
5- Size Uygun sürümü seçin o linke tıklayın ![image](https://user-images.githubusercontent.com/39805679/173199991-d2ce89a4-e7d2-457d-8dd1-c8f40b671122.png) <br>
6- Tıkladık'tan sonra işletim sisteminize göre seçin İşletim sistemize  göre Windows'sa chromedriver_win32.zip seçin ![image](https://user-images.githubusercontent.com/39805679/173200114-ea314a12-fec2-4287-bb63-8d32ee41dd48.png)<br>
7- chromedriver_win32.zip'i tıklayıp indirin  <br>
![image](https://user-images.githubusercontent.com/39805679/173200523-3c4ee671-d6db-4a22-946d-1b336d878609.png)<br>

8- Zip'i açınca Projeye indirdiğiniz klasörüne atın ![image](https://user-images.githubusercontent.com/39805679/173200662-715af02a-ff7d-45fe-abb7-49d09c10e249.png) <br>
9- Artık Google Chrome sürümünüzü başaralı bir şekil de ChromeDriver'ı indirdik.

## Çalışma Mantığı
Not!! Google  açılınca hiç bir şeyle ilgilenmeyin Google ön planda açık kalsın çünkü ekran görüntüsü alırken  başka görüntüler alabilir.

1- İstediğiniz bir esyayı yazdıktan sonra bar dolmakta.  (Telefon Markaları çalışıyor sadece) <br>
2- Google açılmaktadır. Trendyol sitesine gider.<br>
3- Yazdığınız Esyayı arama yerine yazıp o kategoriye gider.<br>
4- Aradığınız  Telefona tıklayıp oraya girer.<br>
5- Konsola fiyatını gösterir.<br>
6- 2 Saniye bekledikten sonra O telefonun ekran görüntüsünü alır.<br>
7- Discord Tarafından oluşturduğumuz Webhook'u sistem bağlanır.<br>
8- Webhook tarafından alınan ekran görüntüsü,ismini ve fiyatını discord kanalına gönderir.<br>
9- Ve sistem başarılı bir şekil de çalışmıştır.<br>
