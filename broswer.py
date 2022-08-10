import sys
import win32ui
import win32gui
from ctypes import windll

from PyQt5.QtWidgets import *
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QUrl, Qt
#from PyQt5.QtWebEngineQuick import QtWebEngineQuick
from PyQt5 import QtCore as qtc
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.showMaximized()
        self.onFeaturePermissionRequested
        
        

        self.setWindowTitle('Fried Yam')
        self.setWindowIcon(QIcon('icons/yamfries.jpg'))
        self.setGeometry(400, 400, 1000, 700)
        #self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        #self.setWindowFlag(qtc.Qt.FramelessWindowHint)
       

        toolbar = QToolBar()
        self.addToolBar(toolbar)
        #self.toolbar.setContextMenuPolicy(False)

        self.backButton = QPushButton()
        self.backButton.setText('Back')
        self.backButton.setIcon(QIcon('icons/back.png'))
        self.backButton.setIconSize(QSize(30,30))
        self.backButton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backButton)
        
        self.forwardButton = QPushButton()
        self.forwardButton.setText('Forward')
        self.forwardButton.setIcon(QIcon('icons/back.png'))
        self.forwardButton.setIconSize(QSize(30,30))
        self.forwardButton.clicked.connect(self.fowardBtn)
        toolbar.addWidget(self.forwardButton)
        
        self.reloadButton = QPushButton()
        self.reloadButton.setText('Reload')
        self.reloadButton.setIcon(QIcon('icons/back.png'))
        self.reloadButton.setIconSize(QSize(30,30))
        self.reloadButton.clicked.connect(self.reloadBtn)
        toolbar.addWidget(self.reloadButton)

        self.homeButton = QPushButton()
        self.homeButton.setText('Home')
        self.homeButton.setIcon(QIcon('icons/back.png'))
        self.homeButton.setIconSize(QSize(30,30))
        self.homeButton.clicked.connect(self.homeBtn)
        toolbar.addWidget(self.homeButton)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        self.webEngineView.setContextMenuPolicy(False)
        initUrl = 'https://www.recipevibes.com/fried-yam-recipe/'
        self.webEngineView.load(QUrl(initUrl))



    def backBtn(self):
       self.webEngineView.back()

    def fowardBtn(self):
       self.webEngineView.forward()

    def reloadBtn(self):
        self.webEngineView.reload()

    def homeBtn(self):
        self.webEngineView.load(QUrl('https://www.recipevibes.com/fried-yam-recipe/'))

    def onFeaturePermissionRequested(self, url, feature):
        if feature in (QWebEnginePage.MediaAudioCapture, 
            QWebEnginePage.MediaVideoCapture, 
    
            QWebEnginePage.MediaAudioVideoCapture):
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)
        else:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionDeniedByUser)




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
