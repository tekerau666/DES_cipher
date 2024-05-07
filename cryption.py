import pyDes
import base64


def encrypt(data, key):
    return base64.b64encode(pyDes.des(key.encode('windows-1251'), pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5).encrypt(data.encode('windows-1251')))


def decrypt(data, key):
    return pyDes.des(key.encode('windows-1251'), pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5).decrypt(base64.b64decode(data)).decode('windows-1251')
