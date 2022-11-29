from wirtschaft import Bestellung
from wirtschaft import Kunde
bestellung_1=Bestellung()
bestellung_1.setmenge(20)
bestellung_1.setpreis("30€")
bestellung_1.setversandkosten("20€")
bestellung_1.setBestellnummer(1234542)
bestellung_1.setbezeichnung("hans")

#print(bestellung_1.getmenge())
#print(bestellung_1.getpreis())

kunde_1=Kunde()

kunde_1.setvorname("hans")
kunde_1.setnachname("Franz")
kunde_1.sete_mail("hans.Franz@gmx.de")
kunde_1.settel_nr(12356743)
kunde_1.setort("Adelsdorf")
kunde_1.sethausnummer(14)
kunde_1.setplz(91325)


bestellung_2=Bestellung()
bestellung_2.setmenge(20)
bestellung_2.setpreis("30€")
bestellung_2.setbezeichnung("schaufel")
bestellung_2.setversandkosten("5€")
bestellung_2.setBestellnummer("17453")

kunde_1.addbestellung(bestellung_1)
kunde_1.addbestellung(bestellung_2)

kunde_1.getbestellungen()






