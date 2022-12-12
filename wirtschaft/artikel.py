class Artikel:
    __artikelnummer=""
    __preis=""
    __bezeichnung=""
    __menge=""
    __MwSt_Satz=""

    def setartikelnummer(self, artikelnummer):
        self.__artikelnummer=artikelnummer
    def getartikelnummer(self):
       return self.__artikelnummer

    def setpreis(self, preis):
        self.__preis=preis
    def getpreis(self):
        return self.__preis

    def setbezeichnung(self, bezeichnung):
        self.__bezeichnung=bezeichnung
    def getbezeichnung(self):
        return  self.__bezeichnung

    def setmenge(self, menge):
        self.__menge=menge
    def getmenge(self):
        return self.__menge

    def setmwst_satz(self, MwSt_satz):
        self.__MwSt_Satz=MwSt_satz
    def getmwst_satz(self):
        return self.__MwSt_Satz
