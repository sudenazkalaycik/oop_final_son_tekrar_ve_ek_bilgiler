"""class color:
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
   """
   
class Person:
    BOLD = '\033[1m' #Bu şekilde tanımlamalar yaparak bold ya da diğer stillerde yazı yazdırabiliyoruz. Ayrıca [...m' kısmında ... yerine gelen kısma gereken renk kodlarını yazarsak ön ve arka plan renkerini değiştirebilir. Önplan için arkaplan gib 8 renk bulunuyor.Seçenekler: kırmızı, yeşil, mavi, morciver, turkuaz ve beyaz. Burada renk kodları 30 (siyah), 31 (kırmızı), 32(yeşil), 33(sarı), 34 (mavi), 35(morciver), 36 (turkuaz),Arkaplan renklerinde de aynı yolu izliyoruz fakat ilk sayı olarak 4 kullanıyoruz ; 40, 41, 42, 43, 44, 45, 46, 47 gibi. İstersek bunları bir classa yazarak da kullanabiliriz.Ör:
    """class color:
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

print(color.BOLD + 'Hello, World!' + color.END)"""
    
    END = '\033[0m'
    def __init__(self):
        self.name = input("Enter your name: ")
        self.surname = input("Enter your surname: ")
        self.yearsOfBird = int(input("Enter your bird day: "))
        self.job = input("Enter your job, if you are a student pleas specify:  ")
        
        
    def calculateAge(self, currentYear):
        result = currentYear - self.yearsOfBird
        return result
        #return f"{self.name} is {result} years old now"
    
    def personalInfo(self):
        print("\n*********\n" + Person.BOLD + "Personal İnformation Board" + Person.END)
        return f"\nName: {self.name} \nSurname: {self.name} \nBird Year: {self.yearsOfBird} \nJob: {self.job} \nAge: {self.calculateAge(2024)}\n" 
    
    
    
    
# sudenaz = Person("Sudenaz", 2005, "Mobil App Developer")
Sudenaz = Person()
print(Sudenaz.personalInfo())

"""print(sudenaz.name)
print(sudenaz.calculateAge(2024))
print(sudenaz.job)
print(sudenaz.yearsOfBird)
"""
#print(sudenaz.personalInfo())


        
        