from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox
from main import Ui_MainWindow
import pygame
from pygame.locals import *
from pygame import mixer
from passgen import Uii_MainWindow

class window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.show()
		self.ui.aboutbutt.clicked.connect(self.about)
		self.ui.musicbutt.clicked.connect(self.music)
		self.ui.startbutt.clicked.connect(self.start)

	def about(self):
		msg = QMessageBox.information(self, "about", "this programm developed by farzad jamshidi at 2 march 2022", QMessageBox.Ok)

	def music(self):
		if self.ui.musicbutt.text() == "music: on":

			# Starting the mixer
			mixer.init()
  
			# Loading the song
			mixer.music.load("/Users/farzad/Downloads/music.mp3")
  
			# Setting the volume
			mixer.music.set_volume(0.7)
  
			# Start playing the song
			mixer.music.play()

			self.ui.musicbutt.setText("music: off")

		elif self.ui.musicbutt.text() == "music: off":
			mixer.music.stop()
			self.ui.musicbutt.setText("music: on")

	def start(self):
		self.startui = start()
		self.startui.show()
		self.close()


class start(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Uii_MainWindow()
		self.ui.setupUi(self)

		


if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	window = window()
	sys.exit(app.exec_())