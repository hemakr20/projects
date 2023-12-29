import pyqrcode
from pyqrcode import QRCode

s = "https://youtube.com/shorts/HMjPZlQAE0E?si=bpWtNz79TqjVzpb-"

url = pyqrcode.create(s)

url.svg("myyoutubeshorts.svg", scale=8)

