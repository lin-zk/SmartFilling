from PyQt5 import Qt
from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from ui.SF_Login import *
from ui.SF_Signup import *
from ui.SF_Loading import *
import picture.ui_resource_rc


class LoginWindow(QDialog, Ui_SF_Login):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(':/logo/icon/logo.png'))


class SignupWindow(QDialog, Ui_SF_Signup):
    def __init__(self, parent=None):
        super(SignupWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("智填_注册")#窗口名
        self.setWindowIcon(QIcon(':/logo/icon/logo.png'))


class LoadingWindow(QMainWindow, Ui_SF_Loading):
    def __init__(self, parent=None):
        super(LoadingWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(':/logo/icon/logo.png'))
        self.setWindowFlags(self.windowFlags())
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        """由于使用.ui文件转换的.py对象的.gif文件无法播放，此处定义loading_gif新对象并在loading中播放"""
        self.loading_gif = QtGui.QMovie(':/loading_icon/loading/big_loading.gif')
        self.loading_gif.setScaledSize(QSize(350, 350))
        self.loading.setMovie(self.loading_gif)
        self.loading_gif.setSpeed(150)
        self.loading_gif.start()
        self.loading2_gif = QtGui.QMovie(':/loading_icon/loading/long_loading.gif')
        self.loading2_gif.setScaledSize(QSize(183, 40))
        self.loading2_gif.setSpeed(200)
        self.loading2.setMovie(self.loading2_gif)
        self.loading2_gif.start()
        self.set_loader()

    def set_loader(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.load_progress_bar)
        self.timer.start(40)

    def load_progress_bar(self):
        self.loading_bar.setValue(self.loading_bar.value() + 1)
        if self.loading_bar.value() <= 5:
            self.tips.setText("智填欢迎您")
        elif self.loading_bar.value() <= 20:
            pass
            self.tips.setText("正在初始化")
        elif self.loading_bar.value() <= 40:
            pass
            self.tips.setText("正在检查网络")
        elif self.loading_bar.value() <= 60:
            pass
            self.tips.setText("正在加载您的数据库")
        elif self.loading_bar.value() <= 80:
            pass
            self.tips.setText("正在加载主页面")
        elif self.loading_bar.value() <= 95:
            pass
            self.tips.setText("正在为您打开")
        elif self.loading_bar.value() < 100:
            self.tips.setText("网页填表，交给智填")
        else:
            self.timer.stop()
            self.tips.setText("")
            self.close()