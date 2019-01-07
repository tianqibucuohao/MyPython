# -*- coding: utf-8 -*-

import qrcode
#from PIL import Image

qrcode.QRCode(
    version=1, 
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    image_factory=None,
    mask_pattern=None)

#qrcode.make('www.baidu.com').save('bai.png')
qrcode.make('www.baidu.com').show()