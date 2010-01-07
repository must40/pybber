# -*- coding: utf-8 -*-
!/usr/bin/env python
import pygtk,gtk,gtk.glade

class okno:
	def __init__(self):
		self.gladefile = "pybber.glade"
		self.wTree = gtk.glade.XML(self.gladefile) 
		# pobieramy główne okno
		self.window = self.wTree.get_widget("window1")
		self.window.show()
		#wyświetlamy głowne okno
		if (self.window):
			self.window.connect("destroy",gtk.main_quit)
		#po zamknięciu okna - kończymy program
		
		#pobranie obiektow z glade i przypisywanie ich do zmiennych:
		self.etykieta=self.wTree.get_widget("label1")
		self.pole=self.wTree.get_widget("entry1")
		
		#tworzymy słownik par - "sygnał":funkcja
		dic={
		"ok": self.ok,
		"wyczysc": self.wyczysc,
		"zamknij": gtk.main_quit}
		
		#i podpinamy go do sygnałow z glade
		self.wTree.signal_autoconnect(dic)
	
	def ok(self,widget):
		#pobieramy sobie wartość pola tekstowego do zmiennej:
		tekst=self.pole.get_text()
		#i zapisujemy go do etykiety - tak po prostu ;)
		self.etykieta.set_text(tekst)
		
	def wyczysc(self,widget):
		self.pole.set_text("")
		self.etykieta.set_text("")
		
if __name__ == "__main__":
	#uruchamiamy okno:
	klasa=okno()
	#uruchamiamy gtk:
	gtk.main()	
