import random,math,time


class player:
    def __init__(self):
        self.sila = 20
        self.dfc = 50
        self.maxhp = 100
        self.spd = 1
        self.ddg = 0
        self.aim = 20
        self.martwy = False
        self.hp = 100
        self.poziom = 0 
        self.xp = 0
        self.start = 5
        self.item = ""
        self.enemy_name = ""
        self.final = False
        self.staznik = True
        self.kanye = True
        self.enemy_sila =  0
        self.enemy_hp = 0
        self.enemy_dfc = 0
        self.enemy_spd = 0
        self.enemy_xp = 0
        self.ammo = 5
        self.bron = ""
        self.sila_broni= 0
        self.ammo_us = 0
        self.aim_broni = 0
        self.miasto_unlocked = False
        self.ucieczka = False
        self.alfabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

class special_item(player):
    def __init__(self):
        super().__init__()
        self.MLG=[]
        self.przedmioty=[]


    def wybor_przedmiotu(self):
        if self.item == "jablko":
            self.jablko()
        elif self.item == "podejrzany_pistolet":
            self.mlg()
        elif self.item == "czarna_pomarancza":
            self.czarna_pomarancza()
        elif self.item == "zolw":
            self.zolw()
        elif self.item == "chipsy":
            self.chipsy()
        elif self.item == "denaturat":
            self.denaturat()
        elif self.item == "lomza":
            self.lomza()

    def jablko(self):
        self.hp += 15
        print("Po zjedzeniu jabłka zostałeś uleczony o 15hp")
        self.special_item.remove("apple")

    def mlg(self):
        print("...")
        self.MLG.append(self.enemy_name)
        self.enemy_hp -= 1000000

    def czarna_pomarancza(self):
        self.aim += 5

    def zolw(self):
        self.dfc += 30

    def chipsy(self):
        self.sila += 10

    def denaturat(self):
        self.sila += 30

    def lomza(self):
        self.hp = self.maxhp

    def finalmlg(self):
        print("...")
        print("...")
        print("...")
        print(self.MLG)
        i = 0
        while i<len(self.MLG):
            if self.MLG[i] == "ork":
                self.ork()
                self.walka()
            elif self.MLG[i] == "grot":
                self.grot()
                self.walka()
            elif self.MLG[i] == "malpa":
                self.malpa()
                self.walka()
            i += 1
        else:
            print("...")

class przeciwnik(special_item):
    def __init__(self):
        super().__init__()
        self.przeciwnicy=["ork", "grot", "malpa"]

    def ork_boy(self):
        self.enemy_sila=20
        self.enemy_hp=40
        self.enemy_dfc=40
        self.enemy_spd=random.randint(0,3)
        self.enemy_xp=random.randint(2,5)
        self.enemy_name="ork"

    def grot(self):
        self.enemy_sila=5
        self.enemy_hp=5
        self.enemy_dfc=5
        self.enemy_spd=random.randint(6,8)
        self.enemy_xp=1
        self.enemy_name="grot"

    def malpa(self):
        self.enemy_sila=10
        self.enemy_hp=25
        self.enemy_dfc=20
        self.enemy_spd=random.randint(3,6)
        self.enemy_xp=random.randint(1,2)
        self.enemy_name="malpa"

class bron(player):
    def __init__(self):
        super().__init__()
        self.guns = ["bolt_pistol", "scar",]
    def wybor_broni(self):
        if self.bron=="bolt_pistol":
            self.sila_broni=15
            self.ammo_us=1
            self.aim_broni=10
        elif self.bron=="scar":
            self.sila_broni=20
            self.ammo_us=2
            self.aim_broni=40

class mechanika(bron, special_item):
    def __init__(self):
        super().__init__()


    def kreator_postaci(self):
        print("Masz do rozdania ", self.start," pkt umiejętności")
        print("W jakich umiejętnościach chcesz je wykorzystać?")
        for i in range(self.start):
            print("1.siła")
            print("2.obrona")
            print("3.szybkość")
            print("4.celność")
            print("5.wytrzymałaść")
            print("6.dodge")
            inp=float(input(""))
            if inp == 1:
                self.sila += 5
                print("twoja siła wzrosła o 5 pkt")
            elif inp == 2:
                self.dfc += 10
                print("twoja obrona wzrosła o 10 pkt")
            elif inp == 3:
                self.spd += 1
                print("twoja prędkość wzrosła o 1 pkt")
            elif inp == 4:
                self.aim += 7
                print("twoja celność wzrosła o 7 pkt ")
            elif inp == 5:
                self.maxhp += 25
                print("twoje punkty zdrowia wzrosły o 25 pkt")
            elif inp == 6:
                self.ddg += 1
                print("twoje dodgowanie wzrosło o 1 pkt")
            else:
                print("nie ma takiej opcji")
                self.start += 1
        print("siła=", self.sila)
        print("obrona=",self.dfc)
        print("prędkość ataku=", self.spd)
        print("celność=", self.aim)
        print("wytrzymałaść=",self.maxhp)
        print("dodge=",self.ddg)
        hp =  self.maxhp / 2   

    def reakcja(self):
        print("wpisz sekwencję, która pojawi się na ekranie, aby uniknąć ataku")
        time.sleep(random.randint(1,3))
        i1=random.randint(0,25)
        i2=random.randint(0,25)
        i3=random.randint(0,25)
        print(self.alfabet[i1],self.alfabet[i2],self.alfabet[i3])
        reakcjalista=[]
        reakcjalista.append(self.alfabet[i1])
        reakcjalista.append(self.alfabet[i2])
        reakcjalista.append(self.alfabet[i3])
        lista="".join(reakcjalista)
        starttime=time.time()
        inp=input().lower()
        endtime=time.time()
        if inp==lista and endtime-starttime<(math.sqrt(self.ddg)+1):
            return True
        else:
            return False

    def walka_twoja_tura(self):
        print("Co chcesz zrobic?")
        print("1-Atak wręcz")
        print("2-Atak zasięgowy")
        print("3-Przedmioty")
        print("4-Ucieczka")
        inp=float(input())
        if inp==1:
            print("atakujesz wręcz")
            self.enemy_hp= self.enemy_hp-self.sila*(random.randint(70,110)/100)*(100/(100 + self.enemy_dfc))
            print("przeciwnikowi zostało",round(self.enemy_hp,2),"hp")
        elif inp==2:
            print("masz",self.ammo,"sztuk amunicji")
            print("czym chcesz strzelić(numer broni na liście)")
            print(self.guns)
            inp=float(input())
            wybor=int(inp-1)
            bron = self.guns[wybor]
            self.wybor_broni()
            if self.ammo < self.ammo_us:
                print("nie masz wystarczająco amunicji")
            else:
                self.ammo -= self.ammo_us
                if self.aim + self.aim_broni>=random.randint(0,100):
                    print("trafiles")
                    self.enemy_hp = self.enemy_hp - self.sila_broni
                    print("twojemu przciwnikowi zostało",round(self.enemy_hp,2),"hp")
                else:
                    print("nie trafiłes")
        elif inp==3:
            print("jakiego przedmiotu chcesz użyc?(numer na liście)")
            print(self.przedmioty)
            inp=float(input())
            wybor=inp-1
            item=self.przedmioty[wybor]
            self.wybor_przedmiotu()
        elif inp==4:
            if self.spd + 50 - self.enemy_spd>random.randint(0,100) and self.final==False:
                print("uciekłeś")
                ucieczka=True
            else:
                print("nie udało ci się uciec")
            if self.final:
                print("nie mozesz uciec z finałowych bitew")
                print("nie bądź tchórzem, Inkwizytorze")

        else:
            print("nie ma takiej opcji")
            self.walka_twoja_tura()
    
    def walka_tura_przeciwnika(self):
        print("Przeciwnik cie atakuje.")
    def c(self):
        print("Atak numer 1")
        self.hp - 10
        print(f"przeciwnik zabrał ci 10hp \n masz teraz {self.hp}")
    
        

    def walka(self):
        print("walczysz z ", self.enemy_name)
        a=input()
        while self.enemy_hp>0:
            if self.spd >= self.enemy_spd:
                print("twój przeciwnik ma",round(self.enemy_hp,2),"hp")
                self.walka_twoja_tura()
                self.walka_tura_przeciwnika()

            else:

                self.walka_tura_przeciwnika()
                print("twój przeciwnik ma",round(self.enemy_hp,2),"hp")
                self.walka_twoja_tura()
            if self.ucieczka and self.final==False:
                    break
            if self.hp<=0:
                print("umarłeś")
                exit()
        if self.enemy_hp<=0:
            self.xp += self.enemy_xp
        self.lvl_up()

    def dodatkowy_punkt_xp(self):
        print("Wydaj 1 punkt umiejętności")
        print("1.siła")
        print("2.obrona")
        print("3.szybkość")
        print("4.celność")
        print("5.wytrzymałaść")
        print("6.dodge")
        inp=float(input(""))
        if inp == 1:
            self.sila+=5
            print("twoje siła wzrosła o 1 pkt")
        elif inp == 2:
            self.dfc+=10
            print("twoja obrona wzrosła o 1 pkt")
        elif inp == 3:
            self.spd+=1
            print("twoja prędkość wzrosła o 1 pkt")
        elif inp == 4:
            self.aim+=7
            print("twoja celność wzrosła o 1 pkt ")
        elif inp == 5:
            self.maxhp+=25
            print("twoje punkty zdrowia wzrosły o 1 pkt")
        elif inp == 6:
            self.ddg+=1
            print("twoje dodgowanie wzrosło o 1 pkt")
        else:
            print ("nie ma takiej opcji ")
            self.dodatkowy_punkt_xp()
        print("siła=",self.sila)
        print("obrona=",self.dfc)
        print("prędkość ataku=",self.spd)
        print("celność=",self.aim)
        print("wytrzymałaść=",self.maxhp)
        print("dodge=",self.ddg)

    def lvl_up(self):
        if self.xp>=2**self.poziom:
            print("---------LEVEL UP---------")
            self.xp-=2**self.poziom
            self.dodatkowy_punkt_xp()
            self.poziom+=1
            if self.poziom%5==0:
                self.dodatkowy_punkt_xp()
                print("dostajesz dodatkowy punkt, ponieważ twój poziom jest podzielny przez 5")
            print("twój poziom to teraz poziom",self.poziom)
        return

class loakcje(mechanika, przeciwnik):
    def intro_gry(self):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        inp = input
        print("TUTAJ BYŁA JAKAŚ HISTORIA ALE TEGO TYPU 150 LINIJEK KODU Z JAKIMIŚ KOLORAMI WIEC UŁATWIE I SKRÓCE")
        inp=input()
        print("JEST GODZINA ",current_time,"")
        inp=input()
        print("TAM JAKIS NAJAZD NA NAS ALE TO MALO WAZNE")
    
    def statek(self):
        print("JAKIES DZIENNIKI I WGL")
        inp=input()
        print("SKIP")
        self.obok_statku()

    def obok_statku(self):
        print("Po prawej stronie widzisz gęsty las, drzewa w nim są iglaste, o barwie niebieskiej. Powiewa z tego miejsca tajemniczością.")
        print("Po lewej stronie zauważyłeś chatkę, która wygląda dosyć przyjaźnie." ,"może będą tam jakieś zapasy...")

        if self.miasto_unlocked:
            print("gdzie idziesz? chatka/las/miasto")
            while True:
                inp=input().upper()
                if inp=="LAS":
                    self.las()
                    break
                elif inp=="CHATKA":
                    self.chatka()
                    break
                elif inp=="MIASTO":
                    self.miasto()
                    break
                else:
                    print("nie ma takiej opcji")
        else:
            print("gdzie idziesz? chatka/las")
            while True:
                inp=input().upper()
                if inp=="LAS":
                    self.las()
                    break
                elif inp=="CHATKA":
                    self.chatka()
                    break
                else:
                    print("nie ma takiej opcji")
    def las(self):
        print("Powoli zmierzasz do lasu...")
        print("Po 5 minutach docierasz do pierwszego drzewa ")
        print("Znajdujesz fioltowe jabłko")
        print("Podnosisz je? T/N")
        while True:
            inp=input().upper()
            if inp=="T":
                if "jablko" in self.przedmioty:
                    print("masz juz jablko")
                else:
                    print("chowasz jabłko w plecaku")
                    self.przedmioty.append("jablko")
                break
            elif inp=="N":
                print("przechodzisz dalej")
                break
            else:
                print("nie ma takiej opcji")

        print("Po chwili spotykasz Małpe")
        inp=input()
        print("Małpa: ugha guha buga")
        inp=input()
        print("Ty: O c**j mu chodzi?")
        inp=input()
        print("walczysz z nim?(tak/nie)")
        while True:
            inp=input().upper()
            if inp =="TAK" or inp=="T":
                print("------ROZPOCZYNASZ WALKE Z MAŁPĄ Z WĄSEM--------")
                self.malpa()
                self.walka()
                print("Patrzysz na małpę która zalewa się krwią z triumfem")
                break
            elif inp=="NIE" or inp=="N":
                print("Ucieczka nie udana, musisz walczyć!")
                self.malpa()
                self.walka()
                break
            else:
                print("nie ma takiej opcji")
        print("Małpa padła z rozwaloną głową")
        print("Dalej idziesz i nic sie nie dzieje")
        print("idziesz... idziesz ... idziesz ...")
        print("Widzisz jakąś złotą poświate za ostatnimi drzewami lasu")
        print("Podchodzisz w kierunku źródła tego światła")
        print("Otwórz/Zostaw")
        inp=input().upper()
        if inp =="OTWÓRZ":
            print('A to ciekawe! Karabin, to chyba Scar. Widziałem tą broń w pradawnej grze "Fortnite"')
            if "scar" in self.guns:
                print("posiadasz już scara")
            else:
                self.guns.append("scar")
                print("bierzesz scara oraz 10 sztuk amunicji do plecaka")
                self.ammo+=10
        else:
            print("przechodzisz obok skrzynki")
            inp=input()
        print("Powoli kończy się las, a w oddali widzisz czubek wieży")
        print("Idziesz do wiezy, czy wracasz do statku Ide/Wracam")
        inp=input().upper()
        if inp =="IDE":
            print("Znajdujesz się przy wieży i czujesz zimne podmuchy powietrza")
            print("Czy dalej chcesz iść w tym kierunku? T/N?")
            inp=input().upper()
            if inp=="T":
                print("*Idziesz do wieży*")
                self.wieza()
            else:
                print("*Bezpiecznie wróciłeś pod statek*")
                self.obok_statku()
        elif inp=="WRACAM":
                print("*Bezpiecznie wracasz pod statek*")
                self.obok_statku()
        else:
            print("Nie mogąc się zdecydować, wróciłeś pod statek. W końcu tam bezpiecznie...")
            self.obok_statku()

    def wieza(self):
        print("*Podbiega do ciebie strażnik wieży*")
        inp=input()
        print("GIŃ LUDZIAKU!!! WAAAAAGH")
        if straznik_wiezy:
            self.ork()
            self.walka()
            straznik_wiezy=False
        print("*Przechodzisz przez drzwi wejsciowe wieży.*")
        print("Masz do wyboru trzy drogi: góra/dół lub powrót, którą wybierasz?")
        while True:
            inp=input().upper()
            if inp == "GÓRA":
                print("wchodzisz po schodach")
                inp=input()
                print("oooh! mało brakowało, prawie się poślizgnąłem!")
                inp=input()
                print("*rozglądasz się*")
                print("W oddali widzisz miasto ")
                miasto_unlocked=True
                print("*schodzisz z powrotem na dół*")
            elif inp == "DÓŁ":
                print("*schodzisz do podziemi po schodach*")
                inp=input()
                print("jesteś w lochach")
                if cum==False:
                    print("Co to Kurwa jest?")
                    print("*Patrzysz na obrzydliwego potwora składającego się z białej, śluzowatej i lepkiej cieczy*")
                    inp=input()
                    print("To monstrum strasznie się lepi! GRYZIE!!!")
                    self.walka()
                    print("*znajdujesz skrzynke z cum pistolem*")
                    cum=True
                    if "cumpistol" in self.guns:
                        print("juz posiadasz ten rodzaj pistoletu")
                    else:
                        self.guns.append("cumpistol")
                else:
                    print("Nic tu więcej nie ma, oprócz białego kleistego śluzu")
            elif inp == "POWRÓT":
                self.las()
                break
            else:
                print("nie ma takiej opcji")
    def miasto(self):
        print("Wchodzisz do miasta")
        print("Po obu stronach widzisz nieźle zachowane budynki, do którego idziesz?")
        inp=input()
        print("Po lewej stronie: <KARCZMA>")
        print("Po prawej stronie: <SKLEP> Z BRONIĄ")
        print("Przed tobą: <FORTECA>")
        inp=input().upper()
        if inp=="KARCZMA":
            self.karczma()
        elif inp =="SKLEP":
            self.sklep()
        elif inp =="FORTECA":
            self.forteca()
        else:
            print("Wiem, że nie jesteś kompasem, ale chyba pomyliłeś kierunki")
            self.miasto()
    def karczma(self):
        print("SPRZEDAWCA: Witaj nieznajomy! Chcesz coś <kupić> czy pójśćć w <spanko> żeby zagoić rany? Możesz również <wyjść>")
        while True:
            inp=input().upper()
            if inp=="SPANKO":
                self.hp= self.maxhp
                print("*przespałeś się z orkiem(?)* Twoje hp wynosi teraz", self.maxhp)
                self.karczma()
                break
            elif inp=="KUPIĆ":
                print("masz",self.przedmioty)
                if self.xp<0:
                    print("spadaj nie masz kasy")
                    break

                else:
                    print("masz",self.xp," xp, ale mozesz się lekko zadłużyć")
                    a=input()
                    print("-------------------cennik----------------------")
                    print("==================jedzenie=====================")
                    print("1.Fioletowe Jablko (hp)  - 5xp")
                    print("2.Czarna Pomarańcza (aim)- 15xp")
                    print("3.Żółw na tarczy (def)   - 30xp")
                    print("4.Chipsy z orka (siła+10)- 30xp")
                    print("===================PICIE=======================")
                    print("5.Denaturat (siła+30) - 100xp")
                    print("6.Łomża(maxhp)-30xp")
                    print("7.WYJŚCIE")
                    while self.xp>=0:
                        inp=str(input())
                        if inp=="1":
                            self.przedmioty.append("jablko")
                            print("pomyślnie zakupiłeś Fioletowe Jablko")
                            self.xp-=5
                        elif inp=="2":
                            self.przedmioty.append("czarna_pomarancza")
                            print("pomyślnie zakupiłeś Czarną Pomarańczę")
                            self.xp-=15
                        elif inp=="3":
                            self.przedmioty.append("zolw")
                            self.xp-=30
                            print("pomyślnie zakupiłeś Żółwia na tarczy")
                        elif inp=="4":
                            self.przedmioty.append("chipsy")
                            print("pomyślnie zakupiłeś Chipsy z orka")
                            self.xp-=30
                        elif inp=="5":
                            self.przedmioty.append("denaturat")
                            print("pomyślnie zakupiłeś Denaturat")
                            self.xp-=100
                        elif inp=="6":
                            self.przedmioty.append("lomza")
                            print("pomyślnie zakupiłeś Łomżę")
                            self.xp-=30
                        elif inp=="7":
                            print("Żegnaj")
                            print("Do zobaczenia")
                            print(self.przedmioty)
                            break
                        else:
                            print("nie ma takiego przedmiotu")
                    else:
                        print("skończyły ci się pieniądze, wróciłeś do karczmy")
                        print(self.przedmioty)
                        self.karczma()
                        break

            elif inp=="WYJŚCIE" or "WYJŚĆ":
                self.miasto()
                break
            else:
                print("nie ma takiej opcji")

    def chatka(self):
        print("Poszedłeś do zauważonej wcześniej chatki")
        print(".")
        print("Jesteś przed drzwiami chatki, 1.wchodzisz czy 2.rozglądasz się? Czy 3 Powrót pod statek")
        while True:
            inp=str(input())
            if inp == "1":
                print("Spotykasz znajomie wyglądającą postać o ciemnoskórej karnacji, oraz szczodrym zaroście")
                inp=input()
                print("nieznajomy: الله عكبار الأم!")
                inp=input()
                print("yy.. Co?")
                inp=input()
                print("Herbatki?")
                inp=str(input())
                if inp=="TAK":
                    print("dobra herbatka leczy twoje wszystkie rany, oraz smutki i niepowodzenia w życiu")
                    self.lomza()

                print("1.A tak w ogóle, to kim ty kurwa jesteś?")
                print("2.Umiesz po rozmawiać po terrańśku?")
                print("3.*skip*")
                inp=str(input())
                if inp == "1":
                    print("A tak w ogóle, to kim ty kurwa jesteś?")
                    inp=input()
                    print("Nieznajomy: Oh! A więc pochodzisz z najświętszej Terry!")
                    inp=input()
                    print("Nieznajomy: Proszę mów mi Stasiek, nie wiesz jak dobrze ujrzeć drugiego człowieka")
                    inp=input()
                    print("A zatem opowiedz mi swoją historię, co tu robisz?")
                    inp=input()
                    print("Stasiek: Sam nie wiem, tyle dni minęło... ")
                    inp=input()
                    print("Stasiek: mówiąc w skrócie, byliśmy normalnymi mieszkańcami, dopóki jakiś wąsacz nie przybył i ni-")
                    inp=input()
                    print("chwila, chwila jaki wąsacz?")
                    inp=input()
                    print("Stasiek: Przez orków zwany jest wielkim przywódcą, jak dla mnie to zwykły prostak")
                    inp=input()
                    print("Stasiek: stylem przypomina Charliego Chaplina ze starożytnych okresów Terry")
                    inp=input()
                    print("Stasiek: Przy okazji, zmienając temat.. znalazłem pistolet")
                    inp=input()
                    print("co? jaki pistolet?")
                    inp=input()
                    print("Stasiek: W legendach mówiono, że jest to broń Bogów, zabije każdego bez wysiłku")
                    inp=input()
                    print("Stasiek: Mółgbym ci go dać, jeśli odpowiesz mi na to pytanie: Podaj mi wzór na pole kwadratu (podpowiedź z potęgą)")
                    inp=str(input()).upper
                    if inp == "A^2":
                        print("Stasiu: To by się zgadzało, oto twoja broń, używaj z rozwagą!")
                        print("otrzymujesz nową broń PODEJRZANY PISTOLET")
                        if "podejrzany_pistolet" in self.przedmioty:
                            print("juz posiadasz ten rodzaj pistoletu")
                        else:
                            self.przedmioty.append("podejrzany_pistolet")
                        print("Stasiu: Podobno Hitler po II wojnie światowej użył go, aby zabić się użył tego pistoletu, ale słuch po jego ciele zaginął..")
                        print("Stasiu: Nie chcę w to wierzyć, ale co jeśli Hitler żyje i to on przejął naszą planetę?")
                        print("Stasiu: W końcu ta podróba Chaplina też mówi po szwabsku, na żołnierzy mówi blitzkriegorks..")
                        print("dzięki, bywaj")
                        print("Stasiu: ja kurwa jestem, nie bywam")
                        print("Dowiadujesz się że tą planetą prawdopodobnie rządzi Hitler, powstała IV rzesza?")
                elif inp == "2":
                    print("Umiesz po rozmawiać po terrańśku?")
                    inp=input()
                    print("Nieznajomy: Na Imperatora, rodowity Terranin!")
                    inp=input()
                    print("Nieznajomy: Pozwól, że się przedstawię, mam na imię Stasiek")
                    inp=input()
                    print("Nie czas na przyjemności, robiłem się jestem Inkwizytorem")
                    inp=input()
                    print("A zatem, Stachu co robisz na tym odludziu? Gdzie reszta mieszkańców?")
                    inp=input()
                    print("Stasiek: Minęło kilka miesięcy od inwazji orków na nasze ziemie, mają nowego przywódcę...")
                    inp=input()
                    print("Stasiek: mówiąc w skrócie, byliśmy normalnymi mieszkańcami, żyliśmy spokojnie... dopóki jakiś wąsaty kutas pojawił się z nikąd i ni-")
                    inp=input()
                    print("-gger Co? Wąsacz? Orkowie nie mają wąsów")
                    inp=input()
                    print("Stasiek: Nie jest to ork, jest to człowiek, zwą go wielkim przywódcą...")
                    print("Stasiek: z wyglądu kogoś mi przypomina... Posiada charakterystyczny wąs")
                    inp=input()
                    print("Kogo ci przypomina? Cywilu")
                    inp=input()
                    print("Stasiek: Hmm pomyślmy... Charliego Chaplina! Inkwizytorze, mam sprawę")
                    inp=input()
                    print("O co chodzi?")
                    inp=input()
                    print("Stasiek: zmienając temat.. znalazłem pistolet... mógłby się Inkwizytorowi przydać")
                    inp=input()
                    print("cywilu, skąd macie pistolet?")
                    inp=input()
                    print("Stasiek: Miasto zostało spustoszone, a ja znalazłem go w ruinach świątyni")
                    print("Stasiek: W legendach mówiono, że jest to broń Bogów, zabije każdego bez wysiłku")
                    inp=input()
                    print("Stasiek: Mówią, że potrzeba wiedzy, by go skutecznie użyć")
                    inp=input()
                    print("Stasiek: Mółgbym Panu go dać, jeśli odpowie mi Pan na to pytanie: Podaj mi wzór na pole kwadratu (podpowiedź z potęgą)")
                    inp=str(input()).upper
                    if inp == "A^2":
                        print("Stasiu: Posiadasz wystarczającą wiedzę, by używać tego pistoletu!")
                        print("Stasiu: To dla Ciebie Inkwizytorze!")
                        if "podejrzany_pistolet" in self.przedmioty:
                            print("juz posiadasz ten rodzaj pistoletu")
                        else:
                            self.przedmioty.append("podejrzany_pistolet")
                        print("Stasiu: Podobno Hitler po II wojnie światowej aby zabić się użył tego pistoletu")
                        inp=input()
                        print("Stasiu: Widocznie nie miał wiedzy, strzelił se w ten pusty łeb")
                        print("Stasiu: Pózniej przejął naszą planetę i prowadzi brutalne rządy orkowie bez przerwy się biją,")
                        inp=input()
                        print("Uważaj na siebie, chwała Imperatorowi")
                        inp=input()
                        print("Stasiu: Niech Imperator będzie z tobą Inkwizytorze")
                    else:
                        print("niepoprawna odpowiedź")

                self.chatka()
                break
            elif inp == "2":
                print("*Rozglądasz się wokół spustoszonego świata...*")
                inp=input()
                print("Spoglądsz na chatkę, jednak po obejrzeniu jej z bliższego dystansu stwierdasz że prędzej możnaby ją nazwać meliną")
                print("*przebiega w tobie myśl: kurwa, jaki menel musi tam mieszkać, to jest po prostu jakaś tragedia!*")
                inp=input()
                print("Przypomina Ci się misja, ŚMIERĆ HERETYKOM!!!")
                inp=input()
                print("nagle dostrzegasz przez okno ciemnoskórego, brodatego humanoida")
                inp=input()
                print("czyli na tej planecie przebywają nie tylko nazistowskie grzyby...")
                self.chatka()
                break
            elif inp == "3":
                self.obok_statku()
            else:
                print("nie ma takiej opcji")
    def sklep(self):
        print("SPRZEDAWCA: Dzień dobry co chciałbyś u nas kupić?")
        while self.xp>=0:
            print("masz dokładnie",self.xp,"xp")
            print("===================cennik=====================")
            print("1.RPG              - 150 xp      ")
            print("2.Snajperka        - 100 xp      ")
            print("3.Latające wąsy    - 200xp   ")
            print("4.rewolwer z oczami- 50xp ")
            print("5.amunicja x50     - 50xp ")
            print("6.wyjście")
            inp=str(input())
            if inp=="1":
                print("pomyślnie zakupiłeś RPG")
                self.guns.append("RPG")
                self.xp-=150
                print("zostało ci tyle",self.xp,"xp")
            elif inp=="2":
                print("pomyślno zakupiłeś Snajperkę")
                self.guns.append("Snajperka")
                self.xp-=150
                print("zostało ci tyle",self.xp,"xp")
            elif inp=="3":
                print("pomyślno zakupiłeś Latające wąsy")
                self.guns.append("Latajace Wasy")
                self.xp-=200
                print("zostało ci tyle",self.xp,"xp")
            elif inp=="4":
                print("pomyślno zakupiłeś rewolwer z oczami")
                self.guns.append("rewolwer")
                self.xp-=50
                print("zostało ci tyle",self.xp,"xp")
            elif inp=="5":
                print("pomyślno zakupiłeś amunicje x50")
                self.ammo=+50
                self.xp-=50
                print("zostało ci tyle",self.xp,"xp")
            elif inp=="6":
                print("powodzenia !")
                print("Bywaj")
                self.miasto()
                break
            else:
                print("nie mamy takiego produktu")

        else:
            print("spadaj nie masz pieniedzy")
    def forteca(self):
        print("*zbliżasz się do fortecy* Czujesz mrok i smród palonych ciał")
        if self.kanye:
            print("Widzisz z daleka pewną czarnoskórą osobę w masce")
        inp=input("Czy na pewno chcesz tam iść? <tak>/<nie>")
        while True:
            if inp=="tak":
                if self.kanye:
                    print("gdy podchodzisz bliżej ta tajemnicza postac zdejmuje maske i mówi:")
                    inp=input()
                    print("Ja kocham wszystkich, mam dość segregacji, uważam że każdy człowiek ma w sobie coś wartościowego.")
                    inp=input()
                    print("PRZEDE WSZYSTKIM HITLER!!!!")
                    inp=input()
                    print("TO KANYE WEST")
                    self.kanye_west()
                    self.walka()
                else:
                    print("*przechodzisz obok zwłok kanye westa i wchodzisz do fortecy*")
                    print("ironia, chyba zabrakło mu oddechu")
                self.forteca_w_srodku()

            elif inp=="nie":
                self.miasto()
                break
            else:
                print("nie ma takiej opcji")

    def sypialnia(self):
        self.szafa=True
        print("*wszedłeś do sypialni*")
        inp=input()
        print("widzisz szafe oraz łóżko")
        inp=input()
        print("WAAAAAGH, PORA LUDZIAKOFI ZROBIĆ BACH Z GUOWY")
        inp=input()
        print( "CHOLERA! Mocno opancerzony ten ork..")
        self.ork_evyboy()
        self.walka()
        print("Gryzie glebę, ale było blisko. Teraz rozejrzę się po pokoju")
        print("najpierw patrzysz na <szafe>/<łóżko>")
        inp=input().upper()
        if inp=="SZAFE":
            print("Kto by się spodziewał, mundury ze swasstykami")
            inp=input()
            print("a co to?")
            inp=input()
            print("w lewym górnym rogu znalazła się amunicja ;D")
            if self.szafa:
                self.ammo+=100
                print("+100 amunicji. Twoja amunicja wynosi teraz",self.ammo)
                inp=input()
                print("Teraz musze zobaczyć co jest pod łóżkiem")
                inp=input()
                print("*spoglądasz pod łóżko i widzisz czyjąś ręke*")
                inp=input()
                print("BOO... pod łożkiem był upiór")
                self.duch()
                self.walka()
                print("Z jakże wielkim wysiłkiem pokonałeś upiora")
                print("Pod łózkiem znajodwała się skrzynia z amunicją")
                self.ammo+=10
                print("otrzymujesz 10 sztuk amunicj i masz",self.ammo)
                self.szafa=False
                self.forteca_w_srodku()
            else:
                print("nic tu juz nie ma")
                self.forteca_w_srodku()
        elif inp=="ŁÓŻKO":
            if self.szafa:
                print("*spoglądasz pod łóżko i widzisz czyjąś ręke*")
                inp=input()
                print("BOO... pod łożkiem był upiór")
                self.duch()
                self.walka()
                print("Pokonałeś upiora, cóż za wyzwanie")
                print("Pod łóżkiem znajdowała się skrzynia z amunicją")
                inp=input()
                print("otrzymujesz +100 sztuk amunicji")
                self.ammo+=100
                print("nie no, teraz muszę zobaczyć, co jest w szafie")
                inp=input()
                print("wow jakie ładne ubrania")
                inp=input()
                print("Same mundury *hatfu*")
                inp=input()
                print("a co to?")
                inp=input()
                print("*w lewym górnym rogu znalazła się amunicja*")
                self.ammo+=10
                print("+10 amunicji. Twoja amunicja wynosi teraz",self.ammo)
                self.szafa=False
                self.forteca_w_srodku()
            else:
                print("nic tu juz nie ma")
                self.forteca_w_srodku()
        else:
            print("Dopadł cię Orkowy ciężki zbrojny chłopak!")
            inp=input()
            print("WAAAAAAAA, ja być duży i zielony!")
            self.sypialnia()
    def kuchnia(self):
        print("*Wchodzisz do kuchni*")
        print("Widzisz rozrzucone i pobite talerze na ziemii")
        inp=input()
        print( "Oho, ktoś tu był...")
        inp=input()
        print("Twoim oczom ukazuje się kobieta!")
        inp=input()
        print("jestem królową tego miejsca!")
        self.kobieta()
        self.walka()
        print("*kobieta pada na ziemię*")
        print("ha, women, idealnie na swoim miejscu... czyli w kuchni")

        inp=input().upper()
        self.forteca_w_srodku()




lokacje = loakcje()
lokacje.intro_gry()

mechaniki = mechanika()
mechaniki.kreator_postaci()

lokacje.statek()