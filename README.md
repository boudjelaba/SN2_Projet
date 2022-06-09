# SN2_Projet

## Code 0

```python
import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        freq_echant = 40
        t_fenetre = 6
        n_data = freq_echant*t_fenetre
        self.xdata = np.arange(0, t_fenetre, 1/freq_echant)
        self.ydata = [np.exp(-self.xdata[i]) for i in range(n_data)]
        self.update_plot()

        self.show()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000/freq_echant)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        self.ydata = self.ydata[1:] + [random.random()]
        self.canvas.axes.cla()
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        self.canvas.draw()

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
```

---
```python
import numpy as np
import time
import matplotlib.pyplot as plt
%matplotlib notebook
plt.rcParams['animation.html'] = 'jshtml'

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i = 0
t = np.linspace(0,2*np.pi,100)
x, y = [], []

while i<100:
    x.append(t[i])
    y.append(np.cos(t[i]))
    
    ax.plot(x, y, color='r')
    
    fig.canvas.draw()  
    ax.set_xlim(0, t.max())
    ax.set_ylim(-1.1,1.1)
    
    time.sleep(0.1)
    i += 1

ax.grid()
```
---

### Code animation graphique 

```python

import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import queue
import numpy as np
import sounddevice as sd
import pdb
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtMultimedia import QAudioDeviceInfo,QAudio,QCameraInfo

input_audio_deviceInfos = QAudioDeviceInfo.availableDevices(QAudio.AudioInput)

class MplCanvas(FigureCanvas):
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		super(MplCanvas, self).__init__(fig)
		fig.tight_layout()

class Animation_plot(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.ui = uic.loadUi('Chemin/mainVsupp.ui',self)
		self.resize(888, 600)
		self.threadpool = QtCore.QThreadPool()	
		self.devices_list= []
		for device in input_audio_deviceInfos:
			self.devices_list.append(device.deviceName())

		
		self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
		self.ui.gridLayout_4.addWidget(self.canvas, 2, 1, 1, 1)
		self.reference_plot = None
		self.q = queue.Queue(maxsize=20)

		self.device = self.devices_list[0]
		self.window_length = 1000
		self.downsample = 1
		self.channels = [1]
		self.interval = 30 
		
		device_info =  sd.query_devices(self.device, 'input')
		self.samplerate = device_info['default_samplerate']
		length  = int(self.window_length*self.samplerate/(1000*self.downsample))
		sd.default.samplerate = self.samplerate
		
		self.plotdata =  np.zeros((length,len(self.channels)))
		
		self.update_plot()
		self.timer = QtCore.QTimer()
		self.timer.setInterval(self.interval) #msec
		self.timer.timeout.connect(self.update_plot)
		self.timer.start()
		self.lineEdit_2.textChanged['QString'].connect(self.update_sample_rate)
		self.lineEdit_3.textChanged['QString'].connect(self.update_down_sample)
		self.lineEdit_4.textChanged['QString'].connect(self.update_interval)
		self.pushButton.clicked.connect(self.start_worker)
		
	def getAudio(self):
		try:
			def audio_callback(indata,frames,time,status):
				self.q.put(indata[::self.downsample,[0]])
			stream  = sd.InputStream( device = self.device, channels = max(self.channels), samplerate =self.samplerate, callback  = audio_callback)
			with stream:
				input()
		except Exception as e:
			print("ERROR: ",e)

	def start_worker(self):
		worker = Worker(self.start_stream, )
		self.threadpool.start(worker)	

	def start_stream(self):
		self.lineEdit_2.setEnabled(False)
		self.lineEdit_3.setEnabled(False)
		self.lineEdit_4.setEnabled(False)
		self.pushButton.setEnabled(False)
		self.getAudio()
		
	def update_now(self,value):
		self.device = self.devices_list.index(value)
		print('Device:',self.devices_list.index(value))

	def update_window_length(self,value):
		self.window_length = int(value)
		length  = int(self.window_length*self.samplerate/(1000*self.downsample))
		self.plotdata =  np.zeros((length,len(self.channels)))
		self.update_plot()

	def update_sample_rate(self,value):
		self.samplerate = int(value)
		sd.default.samplerate = self.samplerate
		length  = int(self.window_length*self.samplerate/(1000*self.downsample))
		self.plotdata =  np.zeros((length,len(self.channels)))
		self.update_plot()
	
	def update_down_sample(self,value):
		self.downsample = int(value)
		length  = int(self.window_length*self.samplerate/(1000*self.downsample))
		self.plotdata =  np.zeros((length,len(self.channels)))
		self.update_plot()

	def update_interval(self,value):
		self.interval = int(value)
		self.timer.setInterval(self.interval) #msec
		self.timer.timeout.connect(self.update_plot)
		self.timer.start()

	def update_plot(self):
		try:
			data=[0]
			
			while True:
				try: 
					data = self.q.get_nowait()
				except queue.Empty:
					break
				shift = len(data)
				self.plotdata = np.roll(self.plotdata, -shift,axis = 0)
				self.plotdata[-shift:,:] = data
				self.ydata = self.plotdata[:]
				self.canvas.axes.set_facecolor((0,0,0))
				
      
				if self.reference_plot is None:
					plot_refs = self.canvas.axes.plot( self.ydata, color=(0,1,0.29))
					self.reference_plot = plot_refs[0]				
				else:
					self.reference_plot.set_ydata(self.ydata)

			
			self.canvas.axes.yaxis.grid(True,linestyle='--')
			start, end = self.canvas.axes.get_ylim()
			self.canvas.axes.yaxis.set_ticks(np.arange(start, end, 0.1))
			self.canvas.axes.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
			self.canvas.axes.set_ylim( ymin=-0.5, ymax=0.5)		
			self.canvas.draw()
		except:
			pass


class Worker(QtCore.QRunnable):

	def __init__(self, function, *args, **kwargs):
		super(Worker, self).__init__()
		self.function = function
		self.args = args
		self.kwargs = kwargs

	@pyqtSlot()
	def run(self):

		self.function(*self.args, **self.kwargs)		


app = QtWidgets.QApplication(sys.argv)
mainWindow = Animation_plot()
mainWindow.show()
sys.exit(app.exec_())

```

---
https://www.youtube.com/watch?v=yFSfcYnP3ZI

---

### GPIO WiringPi

https://www.framboise314.fr/installer-la-derniere-version-de-wiringpi-sur-raspbian-buster/

---

## ECG

https://maker.pro/raspberry-pi/tutorial/how-to-use-a-gps-receiver-with-raspberry-pi-4

https://tutorials-raspberrypi.com/build-raspberry-pi-gps-location-navigation-device/

https://www.instructables.com/Interfacing-GPS-Module-With-Raspberry-Pi/

---

## Email

https://maker.pro/raspberry-pi/projects/how-to-use-the-raspberry-pi4-camera-and-pir-sensor-to-send-emails

---

## GPS

https://www.electronicwings.com/raspberry-pi/gps-module-interfacing-with-raspberry-pi

---

### Code QT

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```

---


### Code Arduino

```cpp
void setup() {
  Serial.begin(9600);
  Serial.println("Initialisation");
  
  analogReference(DEFAULT);
  pinMode(7, OUTPUT);
}
 
void loop() {
  float tensionVide;
  float tensionCharge;
 
  digitalWrite(7, LOW);
  delay(500);
  tensionVide = analogRead(A0)*5.0/1023;
 
  digitalWrite(7, HIGH);
  delay(500);
  tensionCharge = analogRead(A0)*5.0/1023;
 
  Serial.print("Tension à vide = ");
  Serial.print(tensionVide);
  Serial.println("V");
  Serial.print("Tension en charge = ");
  Serial.print(tensionCharge);
  Serial.println("V");
  if (tensionCharge > 1.2) {
    Serial.println("Batterie bonne");
  } else if (tensionCharge > 1.0) {
    Serial.println("Batterie faible");
  } else {
    Serial.println("Batterie à remplacer");
  }
}
```
