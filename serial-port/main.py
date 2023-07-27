import sys
import glob
import serial
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
# from PyQt5 import QtWidgets, QtGui, QtCore

#import pyqtgraph as pg
#import numpy as np
from mydesign import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        #pg.setConfigOption('background', '#f0f0f0')  # 设置背景为灰色
        #pg.setConfigOption('foreground', 'd')  # 设置前景（包括坐标轴，线条，文本等等）为黑色。
        #pg.setConfigOptions(antialias=True) # 使曲线看起来更光滑，而不是锯齿状

        self.setupUi(self)
        # ComboBox
        ports = self.serial_ports()
        baud = ['9600', '19200', '38400', '115200']
        self.comboBox.addItems(ports)
        self.comboBox_2.addItems(baud)
        # 使用 currentIndexChanged() 讓 comboBox 在每次選項改變的時候呼叫 self.display() 這個 function
        # self.comboBox.currentIndexChanged.connect(self.display)
        # self.display()

    # display() 這個 function 的功能在於將當前 comboBox 的選項加入變數
    def display(self):
        """
        Slot documentation goes here.
        """
        self.ui.label_2.setText('你目前選擇的是：%s' % self.ui.comboBox.currentText())

    #@pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        '''
        self.pyqtgraph1.clear() # 清空里面的内容，否则会发生重复绘图的结果
        # 第一种绘图方式
        self.pyqtgraph1.addPlot(title="绘图单条线", y=np.random.normal(size=100),\
            pen=pg.mkPen(color='b', width=2))
        # 第二种绘图方式
        plt2 = self.pyqtgraph1.addPlot(title='绘制多条线')
        plt2.plot(np.random.normal(size=150), pen=pg.mkPen(color='r', width=2),\
            name="Red curve") # pg.mkPen的使用方法，设置线条颜色为红色，宽度为2。
        plt2.plot(np.random.normal(size=110) + 5, pen=(0, 255, 0), name="Green curve")
        plt2.plot(np.random.normal(size=120) + 10, pen=(0, 0, 255), name="Blue curve")
    '''
    # 檢查電腦所有可用的Port
    def serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
