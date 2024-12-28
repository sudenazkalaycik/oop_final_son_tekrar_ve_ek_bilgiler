![Ekran görüntüsü 2024-12-28 174156](https://github.com/user-attachments/assets/419f76ff-5489-48ac-96b3-a025b52ad772)

BOLD = '\033[1m'  ->  print(Person.BOLD + "Personal İnformation Board" + Person.END) ya da print '\033[1m' + 'Hello' ardından print '\033[0m'

Bu şekilde tanımlamalar yaparak bold ya da diğer stillerde yazı yazdırabiliyoruz. 
Ayrıca [...m' kısmında ... yerine gelen kısma gereken renk kodlarını yazarsak ön ve arka plan renkerini değiştirebilir. 
Önplan için arkaplan gib 8 renk bulunuyor.Seçenekler: kırmızı, yeşil, mavi, morciver, turkuaz ve beyaz. 
Burada renk kodları 30 (siyah), 31 (kırmızı), 32(yeşil), 33(sarı), 34 (mavi), 35(morciver), 36 (turkuaz),
Arkaplan renklerinde de aynı yolu izliyoruz fakat ilk sayı olarak 4 kullanıyoruz ; 40, 41, 42, 43, 44, 45, 46, 47 gibi. İstersek bunları bir classa yazarak da kullanabiliriz.Ör:
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   print(color.BOLD + 'Hello, World!' + color.END)

ya da direkt bir değişkene atamadan direkt de kullanabiliriz

