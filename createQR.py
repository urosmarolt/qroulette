import pyqrcode

qr = pyqrcode.create("Stor prut knodl!")
qr.png("testQR.png", scale=3,quiet_zone=5)