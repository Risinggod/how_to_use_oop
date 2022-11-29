class Kunde:
    __vorname=""
    __nachname=""
    __e_mail=""
    __tel_nr=""
    __straße=""
    __hausnummer=""
    __plz=""
    __ort=""
    __bestellungen=[]

    def addbestellung(self, bestellung):
        self.__bestellungen.append(bestellung)

    def stornoalle(self):
        self.__bestellungen.clear()

    def getbestellungen(self):
        return self.__bestellungen

    def setvorname(self, vorname):
        self.__vorname=vorname
    def getvorname(self):
        return self.__vorname

    def setnachname(self, nachname):
        self.__nachname=nachname
    def getnachname(self):
        return self.__nachname

    def sete_mail(self, e_mail):
        self.__e_mail=e_mail
    def gete_mail(self):
        return self.__e_mail

    def settel_nr(self, tel_nr):
        self.__tel_nr=tel_nr
    def gettel_nr(self):
        return self.__tel_nr

    def setstraße(self, straße):
        self.__straße=straße
    def getstraße(self):
        return self.__straße

    def sethausnummer(self, hausnummer):
        self.__hausnummer=hausnummer
    def gethausnummer(self):
        return self.__hausnummer

    def setplz(self, plz):
        self.__plz=plz
    def getplz(self):
        return self.__plz

    def setort(self, ort):
        self.__ort=ort
    def getort(self):
        return self.__ort

    def ausgabe(self):
        print("Vorname: ", self.vorname, "Nachname:", self.nachname, "E-mail:", self.e_mail)

    def uebrbschreiben(self, neu):
        # z.B überprüfen ob ein @ enthalten sind
        self.e_mail=neu







