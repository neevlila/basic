# you need to install first pip to generate qr code
# pip install qrcode

import qrcode

qr = qrcode.make("# enter a message or link to generate qr code")

qr.save("qr.jpg")
