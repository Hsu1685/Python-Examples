import sys
import glob
import serial
from threading import Thread
import time

from PyQt5.QtCore import pyqtSlot, Qt, QStringListModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar, QLineEdit
from PyQt5.QtGui import QPalette
#from PyQt5 import QtWidgets, QtGui, QtCore8

from .serialcompy import SerialCom
from .ui.main_window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.serialcom = SerialCom(baudrate=9600, timeout=0.1, writemode=True)

        self._widget_statusbar()  # 設定statusBar

        # 設定UI初始狀態
        self.label.setText('No Connection')
        self.statusBar.showMessage("No Connection.")

        self.peBackgroundLightGray = QPalette()
        self.peBackgroundLightGray.setColor(QPalette.Background,Qt.lightGray)
        self.peBackgroundGreen = QPalette()
        self.peBackgroundGreen.setColor(QPalette.Background,Qt.green)
        self.label.setPalette(self.peBackgroundLightGray)

        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.lineEdit_2.setEnabled(False)

        self.serial_ports_update()  # 檢查並更新電腦所有可用的Port

        # pushButton連結到function
        self.pushButton.clicked.connect(self.serial_ports_update)
        self.pushButton_2.clicked.connect(self.open_comm)
        self.pushButton_3.clicked.connect(self.close_comm)
        self.pushButton_4.clicked.connect(self.send_text)

        # ComboBox
        #baud = ['9600', '19200', '38400', '115200']
        #self.comboBox_2.addItems(baud)

    def _widget_statusbar(self):
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    # 檢查並更新電腦所有可用的Port
    def serial_ports_update(self):
        ports = self.serialcom.find_comports()
        #self.comport_list = [i[0] for i in ports]  # 取ports中的comport名稱
        self.comport_info = [i[1] for i in ports]  # 取ports中的comport詳細資訊
        self.comboBox.clear()
        self.comboBox.addItems(self.comport_info)

    def closeEvent(self, event):
        self.serialcom.close_comport()
        QApplication.closeAllWindows()  # 關閉主視窗同時關閉所有視窗

    def open_comm(self):
        _device = self.serialcom.devices[self.comboBox.currentIndex()].device
        #print(_device)
        _baudrate = self.lineEdit.text()
        #print(_baudrate)
        if not self.serialcom.register_comport(device=_device):
            print("Cannot specify the comport. Please try again.")
            self.statusBar.showMessage("Cannot specify the comport. Please try again.")
        elif _baudrate.isdecimal() or (_baudrate == ""):
            if _baudrate.isdecimal():
                self.serialcom.serial.baudrate = int(_baudrate)
            try:
                self.serialcom.serial.open()
            except:
                self.statusBar.showMessage("Can't open "+_device)

            if self.serialcom.serial.isOpen(): # open success
                self.label.setText('Opening')
                self.statusBar.showMessage('Opening')
                self.label.setPalette(self.peBackgroundGreen)
                self.comboBox.setEnabled(False)
                self.pushButton.setEnabled(False)
                self.pushButton_2.setEnabled(False)
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.lineEdit_2.setEnabled(True)
                self.statusBar.showMessage("Status: Open "+_device+" successfully.")
                self._start_serialread()
        else:
            print("Text in the baudrate entry is not a number.")
            self.statusBar.showMessage("Text in the baudrate entry is not a number.")

    def _start_serialread(self):
        self._th_sread = Thread(target=self._serial_read)
        self._th_sread.start()

    def _serial_read(self):
        while self.serialcom.serial.is_open:
            try:
                _recv_data = self.serialcom.serial.readline()
            except (TypeError, AttributeError):
                print("Comport disconnected while reading")
                self.statusBar.showMessage("Comport disconnected while reading")
            else:
                if _recv_data != b'':
                    self.listWidget_2.addItem(_recv_data.strip().decode("utf-8"))
                    #time.sleep(1)

    def send_text(self):
        _send_data = self.lineEdit_2.text()
        #print(_send_data)
        self.serialcom.serial.write(_send_data.encode("utf-8"))
        self.listWidget.addItem(_send_data)

    def close_comm(self):
        self.serialcom.close_comport()
        self._th_sread.join()

        if not self.serialcom.serial.isOpen():
            self.label.setText('Disconnected')
            self.statusBar.showMessage('Disconnected')
            self.label.setPalette(self.peBackgroundLightGray)
            self.comboBox.setEnabled(True)
            self.lineEdit.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.lineEdit_2.setEnabled(False)
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
'''
