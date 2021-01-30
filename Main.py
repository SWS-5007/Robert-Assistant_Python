from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import keyboard

os.system('python ./App/GUI.py')


app = QApplication([])
app.setQuitOnLastWindowClosed(False)

icon = QIcon("./Assets/Robert logo.png")

tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

menu = QMenu()
btn = QAction("Home Page")
btn2 = QAction("Robert Listner")
btn.triggered.connect(lambda: os.system('python ./App/GUI.py'))
btn2.triggered.connect(lambda: os.system('python ./App/Robert.pyw'))

menu.addAction(btn)
menu.addAction(btn2)

quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

keyboard.add_hotkey('shift+tab+6', lambda: os.system('python ./App/GUI.py'))
keyboard.add_hotkey(
    'shift+tab+7', lambda: os.system('python ./App/Robert.pyw'))

tray.setContextMenu(menu)
app.exec_()
