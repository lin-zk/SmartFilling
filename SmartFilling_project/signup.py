import os
from uilib import SignupWindow
from admin import AdminWindow
from databaseoperation import Database


class Signup(SignupWindow):
    def __init__(self, parent=None):
        super(Signup, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("智填_注册")  # 窗口名
        self.database = Database('./database/user.db', 0)
        self.admin_win = AdminWindow()  # 创建的用户管理窗口
        self.return_login.clicked.connect(self.Return)
        self.signup.clicked.connect(self.Signup)
        self.help.clicked.connect(self.Help)
        self.signup.setShortcut("Return")  # 设置快捷键
        self.help.setShortcut("Shift+H")  # 设置快捷键
        self.return_login.setShortcut("Shift+R")  # 设置快捷键

    def Return(self):
        self.close()
        self.set_password.setText('')
        self.set_username.setText('')
        self.password_again.setText('')

    def Signup(self):
        username = self.set_username.text()
        password = self.set_password.text()
        confirm = self.password_again.text()
        if not password or not confirm:  # 如果有一个密码或者密码确认框为空
            self.error_tip.setText("❗请设置密码")
        elif self.database.is_has(username):  # 如果用户名已经存在
            self.error_tip.setText("❗您已经注册过了哦，返回登录即可")
        else:
            if password == confirm and password:  # 如果两次密码一致，并且不为空
                if len(username) < 5:
                    self.error_tip.setText("❗用户名长度需五位以上")
                    return
                if len(password) < 6:
                    self.error_tip.setText("❗密码长度需六位以上")
                    return
                else:
                    self.database.insert_table(username, password)  # 将用户信息写入数据库
                    database_name = './database/' + username + '.db'
                    Database(database_name, 1)
                    self.error_tip.setText("")
                    self.close()  # 注册完毕之后关闭窗口
            else:
                self.error_tip.setText("❗两次输入的密码不同")

    def Help(self):
        os.startfile(r".\帮助.pdf")