# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic
import sys

class MyWindow (QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		uic.loadUi("MyForm.ui", self)
		self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyWindow()
	window.show()
	sys.exit(app.exec_())