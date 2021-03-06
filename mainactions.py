#!/usr/bin/python
# -*- coding: utf-8 -*-
from listmanage import *
import gtk,sys,time
from send import *
from connection import *
import commands
from archive import archive_loadlist

def show_hide(self, *widget):  #hide chat
	mainh=self.window.get_size()[1]	
	x,y=self.window.get_position()
	x=(x+400)
	self.recipent=""
	self.window.set_title("Pybber")
	self.window.set_gravity(gtk.gdk.GRAVITY_SOUTH_EAST)
	self.leftwindow.hide()
	self.window.resize(300,mainh)
	self.window.present()
	self.archivewindow.hide()
	self.archivelist.hide()
	self.archivescroll.hide()
	self.pos=self.window.get_position()	
	
def clear(self, *widget):
	if self.recipent in self.messages:
		self.messages[self.recipent]=""
		loadchat(self,self.recipent)	
		
def notification(self,user,text):
	title="Nowa wiadomość od "+user
	try:
		self.n.update(title=title,body=text)
	except:
		self.n = pynotify.Notification(title, text)  
		self.n.attach_to_status_icon(self.staticon)
	self.n.show()
	
def set_online(self,widget):
	desc=self.desc.get_text()
	self.connection.set_status(0,desc)
	self.statusbar.set_active(0)
def set_away(self,widget):
	desc=self.desc.get_text()
	self.connection.set_status(1,desc)
	self.statusbar.set_active(1)
def set_xa(self,widget):
	desc=self.desc.get_text()
	self.connection.set_status(2,desc)
	self.statusbar.set_active(2)
def set_dnd(self,widget):
	desc=self.desc.get_text()
	self.connection.set_status(3,desc)
	self.statusbar.set_active(3)
def set_chat(self,widget):
	desc=self.desc.get_text()
	self.connection.set_status(4,desc)
	self.statusbar.set_active(4)
def set_invisible(self,widget):
	desc=self.desc.get_text()
	self.connection.set_status(5,desc)
	self.statusbar.set_active(5)
	

def logon(self,*widget):
	jid=self.login.get_text()
	pwd=self.passwd.get_text()
	self.connection.connect_init(self,jid,pwd)
	self.settings.saveacc(self)
	self.loginbox.hide()
	self.jidlabel.set_label(jid)	
	self.staticon.set_from_file("icons/disconnected.png") 
	
def changedata(self, *widget):
	self.toolong.hide()
	self.loginbox.show()
	self.not_connected.hide()

def send(self,*widget):
	sendmsg(self)

def chdesc(self,*widget):
	desc=self.desc.get_text()
	index=self.statusbar.get_active()
	self.connection.set_status(index,desc)

def chstatus(self,widget):
	desc=self.desc.get_text()
	index=self.statusbar.get_active()
	self.connection.set_status(index,desc)
	
def hidewarn(self,widget):
	self.toolong.hide()

def reconnect(self,widget):
	self.connection.reconnect()

def reconnect2(self,widget):
	self.connection.reconnect2()

def resize(self,widget):
	self.posx,self.posy=self.window.get_position()
	#  self.renderer.props.wrap_width = int(self.column.get_width())-int(10)

def close(self,*widget):
	self.connection.cl=None
	self.connection=None
	gtk.main_quit()
	sys.exit(0)

def icohide(self, event,widget):
	self.posx,self.posy=self.window.get_position()
	self.window.hide()
	self.hidden=True
	return True
	window.connect('delete-event', hide_window)

def loadFinished(self,a,*b):
	self.chat.execute_script("scroll();")

	
def savesettings(self,widget):
	self.settings.save(self)
		
def closesettings(self,widget):
	self.window.set_gravity(gtk.gdk.GRAVITY_SOUTH_WEST)
	self.wTree.get_widget('frame1').hide()
	mainh=self.window.get_size()[1]	
	self.window.resize(300,mainh)

def opensettings(self,widget):
	self.window.set_gravity(gtk.gdk.GRAVITY_SOUTH_WEST)
	self.wTree.get_widget('frame1').show()
	self.wTree.get_widget('combobox2').set_active(self.settings.show)
	self.wTree.get_widget('entry8').set_text(self.settings.status)
	self.wTree.get_widget('entry11').set_text(self.settings.me)

def activate(self,widget):
	if not self.window.is_active():
		self.window.present()
		self.window.show()		
		self.staticon.set_blinking(False)
		if self.hidden:
			self.window.move(self.posx,self.posy)
		self.hidden=False
	if self.window.is_active():
		self.window.present()
		self.posx,self.posy=self.window.get_position()
		self.window.hide()
		self.hidden=True

def iconmenu(self,widget, button, time, test = None):
	if button == 3:
		if test:
			self.iconpopup.show_all()
			self.iconpopup.popup(None, None, None, 3, time)
		
def chatfocus(self, *widget):
	if self.window.get_default_widget()==None:
		self.staticon.set_blinking(False)
		self.window.set_urgency_hint(False)

def contactmenu(self, treeview, event):
	if event.button == 3:
		x = int(event.x)
		y = int(event.y)
		time = event.time
		pthinfo = treeview.get_path_at_pos(x, y)
		if pthinfo is not None:
			path, col, cellx, celly = pthinfo
			treeview.grab_focus()
			treeview.set_cursor( path, col, 0)
			self.staticon.set_blinking(False)
			self.contactpopup.popup( None, None, None, 3, time)
			return True
				
def link(self,widget,frame,request,navigation_action,policy):
	commands.getoutput("xdg-open "+request.get_uri())
	

def archive(self, *widget):
	self.archivewindow.show()
	archive_loadlist(self)
	self.archivelist.show()
	self.archivescroll.show()
	self.leftwindow.show()
	
def closearchive(self, *widget):
	mainh=self.window.get_size()[1]
	self.window.set_gravity(gtk.gdk.GRAVITY_SOUTH_EAST)
	self.archivewindow.hide()
	self.window.set_title("Rozmowa z "+self.recipentname+" ("+self.recipent+")")
	loadchat(self,self.recipent)
	self.message.grab_focus()
	self.posx,self.posy=self.window.get_position()
	self.loadFinished('','')
	self.wTree.get_widget("hbox2").show()
	item = self.listmodel.get_iter_first ()
	while ( item != None ):
		if self.listmodel.get_value(item, 4)==self.archiveopen: 
			close=item
		item =self.listmodel.iter_next(item)
	close=self.listmodel[close]
	show_back(self,close)
	self.archiveopen=""

def zoomin(self,widget):
	self.chat.zoom_in()
	
def zoomout(self,widget):
	self.chat.zoom_out()
