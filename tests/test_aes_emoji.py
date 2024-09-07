# Test AES to emoji encoding and decoding.

from db.emoji import encode, decode
from db.aes import encrypt, decrypt
import unittest

class TestAESEmoji(unittest.TestCase):

    def test_aes_to_emoji(self):
        # Test with a single character
        plain_text = "a"
        password = "secretpassword"
        enc = encrypt(plain_text, password)
        enc['cipher_text']= encode(enc['cipher_text'])
        enc['cipher_text'] = decode(enc['cipher_text'])
        dec = decrypt(enc, password)
        self.assertEqual(dec, plain_text)

        # Test with a longer string
        plain_text = "Hello, World!"
        password = "secretpassword"
        enc = encrypt(plain_text, password)
        enc['cipher_text']= encode(enc['cipher_text'])
        enc['cipher_text'] = decode(enc['cipher_text'])
        dec = decrypt(enc, password)
        self.assertEqual(dec, plain_text)

        # Test with an empty string
        plain_text = ""
        password = "secret password"
        enc = encrypt(plain_text, password)
        enc['cipher_text']= encode(enc['cipher_text'])
        enc['cipher_text'] = decode(enc['cipher_text'])
        dec = decrypt(enc, password)
        self.assertEqual(dec, plain_text)

        # Test with numbers
        plain_text = "1234567890"
        password = "secretpassword"
        enc = encrypt(plain_text, password)
        enc['cipher_text']= encode(enc['cipher_text'])
        enc['cipher_text'] = decode(enc['cipher_text'])
        dec = decrypt(enc, password)
        self.assertEqual(dec, plain_text)

        # Test with special characters
        plain_text = "!@#$%^&*()"
        password = "secretpassword"
        enc = encrypt(plain_text, password)
        enc['cipher_text']= encode(enc['cipher_text'])
        enc['cipher_text'] = decode(enc['cipher_text'])
        dec = decrypt(enc, password)
        self.assertEqual(dec, plain_text)

        # Test with mixed characters
        plain_text = "Hello, World! 1234567890 !@#$%^&*()"
        password = "secretpassword"
        enc = encrypt(plain_text, password)
        enc['cipher_text']= encode(enc['cipher_text'])
        enc['cipher_text'] = decode(enc['cipher_text'])
        dec = decrypt(enc, password)
        self.assertEqual(dec, plain_text)


if __name__ == '__main__':
    unittest.main()