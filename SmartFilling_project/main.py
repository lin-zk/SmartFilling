import os
from ui.SF_Main import *
from webbrowser import open_new_tab
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QAbstractItemView, QTableWidgetItem, QWidget \
    , QCheckBox, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QSize
from databaseoperation import Database


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, username, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(':/logo/icon/logo.png'))
        self.setWindowTitle(username + "，智填欢迎您！")  # 窗口名
        self.username = username
        self.database_name = './database/' + username + '.db'
        self.database = Database(self.database_name, 1)
        self.select_all_flag = False  # 是否选择全部
        self.check_list = []  # 保存所有的选择框
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.white)  # 设置窗口背景颜色
        self.setPalette(palette)
        self.select_all.setIcon(QIcon(':/tool_icon/tool/select_all.png'))
        self.select_all.setIconSize(QSize(40, 40))
        self.delete_2.setIcon(QIcon(':/tool_icon/tool/delete.png'))
        self.delete_2.setIconSize(QSize(35, 35))
        self.add.setIcon(QIcon(':/tool_icon/tool/add.png'))
        self.add.setIconSize(QSize(35, 35))
        self.refresh.setIcon(QIcon(':/tool_icon/tool/refresh.png'))
        self.refresh.setIconSize(QSize(35, 35))
        self.clear.setIcon(QIcon(':/tool_icon/tool/clear.png'))
        self.clear.setIconSize(QSize(35, 35))
        self.table()
        self.get_all_info()  # add table 之后才有show
        self.button()  # 添加按钮并绑定事件
        self.set_timer()
        self.select_all.setShortcut("Ctrl+A")  # 设置快捷键
        self.delete_2.setShortcut("Backspace")
        self.add.setShortcut("Ctrl+N")
        self.refresh.setShortcut("F5")
        self.clear.setShortcut("Ctrl+Backspace")

    def set_timer(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.set_select_all_icon)
        self.timer.timeout.connect(self.edit_unable)
        self.timer.start(0)

    def set_select_all_icon(self):
        choose_list = []
        for i in self.check_list:
            if i.isChecked():
                choose_list.append(i)
        if len(choose_list) == self.datatable.rowCount():
            self.select_all.setIcon(QIcon(':/tool_icon/tool/select_all_nothing.png'))
            self.select_all.setIconSize(QSize(35, 35))
            self.select_all_flag = True
        else:
            self.select_all.setIcon(QIcon(':/tool_icon/tool/select_all.png'))
            self.select_all.setIconSize(QSize(40, 40))
            self.select_all_flag = False

    def edit_unable(self):
        self.rowcount = self.datatable.rowCount()
        for i in range(self.rowcount):
            item4 = self.datatable.item(i, 4)
            if item4 == None:
                item4 = QtWidgets.QTableWidgetItem()
                self.datatable.setItem(i, 4, item4)
            item5 = self.datatable.item(i, 5)
            if item5 == None:
                item5 = QtWidgets.QTableWidgetItem()
                self.datatable.setItem(i, 5, item5)
            item6 = self.datatable.item(i, 6)
            if item6 == None:
                item6 = QtWidgets.QTableWidgetItem()
                self.datatable.setItem(i, 6, item6)
            item4.setFlags(QtCore.Qt.ItemFlag(1))
            item5.setFlags(QtCore.Qt.ItemFlag(32))
            item6.setFlags(QtCore.Qt.ItemFlag(32))

    def table(self):
        """添加数据表格"""
        self.datatable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动填充
        self.datatable.setSelectionBehavior(QAbstractItemView.SelectRows)  # 只能选择整行
        self.datatable.setColumnCount(7)  # 设置列数
        self.datatable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.datatable.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.datatable.setHorizontalHeaderLabels(["", "网址", "关键字", "填充内容", "写入时间", "修改时间",""])  # 设置首行
        self.datatable.verticalHeader().hide()  # 把序号隐藏

    def get_all_info(self):
        """获取所有的用户信息"""
        data = self.database.read_table(1)
        for info in data:
            self.add_row(info[0], info[1], info[2], info[3], info[4])

    def add_row(self, url, key, info, created_time, change_time):
        """在表格上添加一行新的内容"""
        self.datatable.blockSignals(True)  # 由于这里会触发信号槽，所以我们先阻断信号
        row = self.datatable.rowCount()  # 表格的行数
        self.datatable.setRowCount(row + 1)  # 添加一行表格
        self.datatable.setItem(row, 1, QTableWidgetItem(str(url)))  # 将用户信息插入到表格中
        self.datatable.setItem(row, 2, QTableWidgetItem(str(key)))
        self.datatable.setItem(row, 3, QTableWidgetItem(str(info)))
        self.datatable.setItem(row, 4, QTableWidgetItem(str(created_time)))
        self.datatable.setItem(row, 5, QTableWidgetItem(str(change_time)))
        self.datatable.setItem(row, 6, QTableWidgetItem("🌏"))
        # 设置复选框
        widget = QWidget()
        check = QCheckBox()
        self.check_list.append(check)  # 添加到复选框列表中
        check_lay = QHBoxLayout()
        check_lay.addWidget(check)
        check_lay.setAlignment(Qt.AlignCenter)
        widget.setLayout(check_lay)
        self.datatable.setCellWidget(row, 0, widget)
        self.datatable.blockSignals(False)  # 打开信号

    # 获取选中行列、内容
    def to_database(self, row, col):
        if col == 0 or col == 4 or col == 5 or col==6:
            return
        else:
            key_item = self.datatable.item(row, 4)
            info_item = self.datatable.item(row, col)
            info = info_item.text()
            key = key_item.text()
            if col == 1:
                info_db = 'url'
            if col == 2:
                info_db = 'key'
            if col == 3:
                info_db = 'info'
            self.database.update_table_by_time(info_db, key, info)
            self.database.update_table_by_time("change_time", key, self.database.get_time())
            self.datatable.item(row, 5).setText(self.database.get_time())

    def button(self):
        '''在这里绑定信号和槽'''
        self.select_all.clicked.connect(self.select_fun)
        self.delete_2.clicked.connect(self.delete_fun)
        self.add.clicked.connect(self.add_fun)
        self.refresh.clicked.connect(self.refresh_fun)
        self.clear.clicked.connect(self.clear_fun)
        self.browser.clicked.connect(self.to_browser_fun)

        self.datatable.cellChanged.connect(self.to_database)
        self.datatable.cellClicked.connect(self.url_to_browser)

        self.help.triggered.connect(self.Help)
        self.about.triggered.connect(self.About)
        self.night.triggered.connect(self.Night)
        self.day.triggered.connect(self.Day)

    def select_fun(self):
        """选择是否选择全部"""
        if not self.select_all_flag:
            for check in self.check_list:
                check.setCheckState(2)  # 设置为选择状态
                self.select_all.setIcon(QIcon(':/tool_icon/tool/select_all.png'))
                self.select_all.setIconSize(QSize(40, 40))
            self.select_all_flag = True
        else:
            for check in self.check_list:
                check.setCheckState(0)  # 设置为未选状态
                self.select_all.setIcon(QIcon(':/tool_icon/tool/select_all_nothing.png'))
                self.select_all.setIconSize(QSize(35, 35))
            self.select_all_flag = False

    def delete_fun(self):
        choose_list = []
        for i in self.check_list:
            if i.isChecked():
                choose_list.append(i)
        if choose_list:
            pass
        else:
            return
        answer = QMessageBox.question(self, '提示', '确定删除', QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if answer == QMessageBox.Yes:
            pass
        if answer == QMessageBox.Cancel:
            return
        for i in choose_list:
            url = self.datatable.item(self.check_list.index(i), 1).text()
            self.database.delete_table_by_username(url, 1)
            self.datatable.removeRow(self.check_list.index(i))
            self.check_list.remove(i)

    def add_fun(self):
        """一行一行的添加数据"""
        time = self.database.get_time()
        self.add_row("", "", "", time, time)
        self.database.insert_table1("", "", "", time, time)

    def refresh_fun(self):
        self.datatable.clearContents()
        self.check_list.clear()
        self.datatable.setRowCount(0)
        self.database.create_table(1)
        self.get_all_info()
        QMessageBox.about(self, '提示', '刷新成功')

    def clear_fun(self):
        if self.datatable.rowCount() == 0:
            return
        else:
            pass
        answer = QMessageBox.warning(self, '提示', '确定清空？该操作不可撤回', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if answer == QMessageBox.Yes:
            pass
        if answer == QMessageBox.No:
            return
        self.database.clear()  # 清空数据库数据
        self.datatable.clearContents()  # 清空表格的内容
        self.datatable.setRowCount(0)  # 将表格的行数重置为0
        self.check_list = []

    def to_browser_fun(self):
        open_new_tab("https://cn.bing.com/")

    def Help(self):
        os.startfile(r".\帮助.pdf")  # 弹出帮助文件

    def About(self):
        os.startfile(r".\关于.pdf")  # 弹出关于文件

    def Night(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.black)  # 设置窗口背景颜色
        self.setPalette(palette)

    def Day(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.white)  # 设置窗口背景颜色
        self.setPalette(palette)

    def url_to_browser(self, row, col):
        if col==6:
            url=self.datatable.item(row, 1).text()
            open_new_tab(url)
        else: return
