import qrcode
from PIL import Image
import time
face = Image.open('beyazlogo.jpeg')
qr_big = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
face = face.resize((70,70))
qr_big.add_data('Hello World')   #qr code data
qr_big.make()
img_qr_big = qr_big.make_image().convert('RGB')
pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2) 
img_qr_big.paste(face, pos)
img_qr_big.save('qr.png')  #file name