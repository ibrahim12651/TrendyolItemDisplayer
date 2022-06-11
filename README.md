# Esya_Fiyati_Gosterimi
Telefon Markalarından istediğinizi yazıp size ismini ve fiyatını bir de fotosunu atacaktır.



![image](https://user-images.githubusercontent.com/39805679/173198149-5a9b9636-8e2f-4f91-83f0-6586fe076b6f.png)

Bu modülleri indirmeniz gereklidir yoksa çalışmaz!

pip install selenium <br>
pip install pyautogui <br>
pip install discord-webhook <br>
pip install progress <br>

time ve os modülleri python da kendiliğin de vardır.

## Google Sürümü Kontrol Etme

1- Google açın 3 noktalıya tıklayıp ayarlara tıklayın <br>
2- Chrome hakkındaya tıklayın <br>
![image](https://user-images.githubusercontent.com/39805679/173199033-a7417c5c-6b4e-44b8-9e9f-d652287d471e.png) <br>
3- Chrome hakkındaya tıkladıktan sonra  sürümü gösterilir <br>
![image](https://user-images.githubusercontent.com/39805679/173199204-a7c6bafb-b664-4112-a305-ddb149820309.png) <br>
4- [ChromeDriver](https://chromedriver.chromium.org/downloads) – Verdiğim linke tıklayıp chromedriver sitesine gidersiniz oradan size uygun sürümü bulup indirin <br>
5- Size Uygun sürümü seçin o linke tıklayın ![image](https://user-images.githubusercontent.com/39805679/173199991-d2ce89a4-e7d2-457d-8dd1-c8f40b671122.png) <br>
6- Tıkladık'tan sonra işletim sisteminize göre seçin İşletim sistemize  göre Windows'sa chromedriver_win32.zip seçin ![image](https://user-images.githubusercontent.com/39805679/173200114-ea314a12-fec2-4287-bb63-8d32ee41dd48.png)<br>


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
