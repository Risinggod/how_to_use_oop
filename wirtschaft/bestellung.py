#Beschreibung der klassen
class Bestellung:
    __menge= ""
    __preis= ""
    __versandkosten= ""
    __Bestellnummer= ""
    __bezeichnung= ""
    __artikel=[]

    def add_artikel(self, artikel):
        self.__artikel.append(artikel)
    def get_artikel(self):
        return self.__artikel
    #konstruktor
    def __init__(self):
        print("objekt wurde erzeugt")

    #Setter, Getter Funktionen setzen
    def setmenge(self, menge):
        self.__menge=menge

    def getmenge(self):
        return self.__menge

    def setpreis(self, preis):
        self.__preis = preis

    def getpreis(self):
        return self.__preis

    def setversandkosten(self, versandkosten):
        self.__versandkosten = versandkosten

    def getversandkosten(self):
        return self.__versandkosten

    def setBestellnummer(self, Bestellnummer):
        self.__Bestellnummer = Bestellnummer

    def getBestellnummer(self):
        return self.__Bestellnummer

    def setbezeichnung(self, bezeichnung):
        self.__bezeichnung = bezeichnung

    def getbezeichnung(self):
        return self.__bezeichnung














