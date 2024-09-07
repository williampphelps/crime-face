# Description: AES encryption and decryption functions
# Will be used by a backend api to encrypt/decrypt posts

from db.emoji import decode, encode

import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import os


# Pad with PKCS7
def pad(s):
    block_size = 16
    padding_needed = block_size - len(s) % block_size
    return s + bytes([padding_needed] * padding_needed)

# Remove PKCS7 padding
def unpad(s):
    return s[:-s[-1]]

def encrypt(plain_text, password):
    salt = os.urandom(AES.block_size)
    iv = Random.new().read(AES.block_size)
    private_key = hashlib.scrypt(password.encode('utf-8'), salt=salt, n=2**14, r=8, p=1, dklen=32)
    padded_text = pad(plain_text.encode('utf-8'))
    cipher_config = AES.new(private_key, AES.MODE_CBC, iv)
    cipher_text = cipher_config.encrypt(padded_text)
    return {
        'cipher_text': base64.b64encode(cipher_text).decode(),
        'salt': base64.b64encode(salt).decode(),
        'iv': base64.b64encode(iv).decode()
    }

def decrypt(enc_dict, password):
    salt = base64.b64decode(enc_dict['salt'])
    iv = base64.b64decode(enc_dict['iv'])
    enc = base64.b64decode(enc_dict['cipher_text'])
    private_key = hashlib.scrypt(password.encode('utf-8'), salt=salt, n=2**14, r=8, p=1, dklen=32)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(enc)
    original = unpad(decrypted).decode('utf-8')
    return original