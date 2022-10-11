import os
import sys
from uilib import LoginWindow
from signup import Signup
from uilib import LoadingWindow
from main import MainWindow
from admin import AdminWindow
from databaseoperation import Database
from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog


class Login(LoginWindow):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("智填_登录")  # 窗口名
        self.database = Database('./database/user.db', 0)
        self.admin_win = AdminWindow()  # 创建的用户管理窗口
        self.sign_up_win = Signup()
        self.login.clicked.connect(self.Login)
        self.sign_up.clicked.connect(self.Signup)
        self.help.clicked.connect(self.Help)
        self.login.setShortcut("Return")  # 设置快捷键
        self.help.setShortcut("Shift+H")  # 设置快捷键
        self.sign_up.setShortcut("Shift+S")  # 设置快捷键

    def Login(self):
        username = self.username.text()
        password = self.password.text()
        data = self.database.find_password_by_username(username)  # 在数据库中查找数据
        if username and password:  # 如果两个输入框都不为空
            if data:
                if str(data[0][0]) == password:
                    self.password.setText('')  # 登录成功，将之前的用户信息清除
                    self.username.setText('')
                    self.close()
                    if username == 'admin':  # 如果是管理员，进入管理界面
                        self.database.update_time(username)
                        self.error_tip.setText("")
                        self.admin_win.show()
                    else:
                        self.database.update_time(username)
                        self.error_tip.setText("")
                        self.main_win = MainWindow(username)
                        self.main_win.show()
                        self.main_win.change.triggered.connect(self.Change)
                        self.main_win.destroy1.triggered.connect(self.Destory)
                        self.main_win.password.triggered.connect(self.Password)
                        self.loading_win = LoadingWindow()  # 登录后的加载页
                        self.loading_win.show()
                else:
                    self.error_tip.setText("❗用户名或密码错误")
            else:
                self.error_tip.setText("❗用户名或密码错误")
        elif username:  # 如果用户名写了
            self.error_tip.setText("❗请输入密码")
        else:
            self.error_tip.setText("❗请输入账号")

    def Signup(self):
        self.hide()  # 隐藏登录页面
        self.password.setText('')
        self.username.setText('')
        self.sign_up_win.show()  # 展示注册页面
        self.sign_up_win.exec_()
        self.show()

    def Help(self):
        os.startfile(r".\帮助.pdf")  # 弹出帮助文件

    def Change(self):
        self.main_win.close()
        username = self.main_win.username
        self.database.delete_table_by_username(username)
        os.remove(r'./database/' + username + '.db')  # 删除用户个人数据库
        self.show()

    def Destory(self):
        answer = QMessageBox.warning(self, '提示', '确定注销？该操作不可撤回', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if answer == QMessageBox.Yes:
            pass
        if answer == QMessageBox.No:
            return
        self.main_win.close()
        username = self.main_win.username
        self.database.delete_table_by_username(username)
        os.remove(r'./database/' + username + '.db')  # 删除用户个人数据库
        self.show()

    def Password(self):
        username = self.main_win.username
        password, ok = QInputDialog.getText(self, "修改密码", "请输入新密码")
        if ok and password:
            if len(password) >= 6:
                self.database.update_table(username, password)
            else:
                QMessageBox.critical(self, "警告", "密码长度需大于6位", QMessageBox.Ok, QMessageBox.Ok)


app = QApplication(sys.argv)
window = Login()
window.show()
sys.exit(app.exec_())
