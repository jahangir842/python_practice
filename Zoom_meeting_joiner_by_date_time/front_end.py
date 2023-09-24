from PyQt5 import QtGui, uic ,QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import sys
from time import strftime
from subprocess import call
import webbrowser

root = os.path.expanduser('~')
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('fornt_end.ui', self)
        self.show()
        # self.setupUi(self)
        self.btn1.clicked.connect(self.ftn)

        # self.label.setText("Please select audio process Mode...")

    def ftn(self):
        time_text = self.time_txt.text()
        link_text = self.link_txt.text()

        print(time_text)
        print(link_text)
        system_time = strftime("%m/%d/%Y %H:%M")
        print(system_time)
        with open('./utilts/meeting_time.txt', 'w') as f:
            f.write(time_text)
        with open('./utilts/meeting_link.txt', 'w') as f:
            f.write(link_text)
        hint = "true"
        while hint == "true":
            if strftime("%m/%d/%Y %H:%M") == time_text:
                webbrowser.open(link_text, new=2)
                hint = "false"
                exec(open('Screen-Recorder-in-Python/main.py').read())
        print("Meeting time passed, Please schedule new meeting")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
