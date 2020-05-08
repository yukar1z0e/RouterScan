from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.left_xxx = QtWidgets.QPushButton(" ")
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "遇到问题")
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "关注我们")
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "反馈建议")
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='white'), "我的收藏")
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.download', color='white'), "下载管理")
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), "本地音乐")
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.film', color='white'), "热门MV")
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy', color='white'), "在线FM")
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.music', color='white'), "华语流行")
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_2 = QtWidgets.QPushButton("我的音乐")
        self.left_label_1 = QtWidgets.QPushButton("每日推荐")
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget.setObjectName('left_widget')
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.left_label_1.setObjectName('left_label')
        self.left_label_2.setObjectName('left_label')
        self.left_label_3.setObjectName('left_label')

        self.left_button_1.setObjectName('left_button')
        self.left_button_2.setObjectName('left_button')
        self.left_button_3.setObjectName('left_button')
        self.left_button_4.setObjectName('left_button')
        self.left_button_5.setObjectName('left_button')
        self.left_button_6.setObjectName('left_button')
        self.left_button_7.setObjectName('left_button')
        self.left_button_8.setObjectName('left_button')
        self.left_button_9.setObjectName('left_button')

        self.right_widget.setObjectName('right_widget')
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
