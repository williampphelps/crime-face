import unittest
import sys
sys.path.append('./')
from db.aes import encrypt, decrypt

class TestAES(unittest.TestCase):
    """
    Test case for AES encryption and decryption.
    """

    def test_encrypt(self):
        """
        Test the encrypt function.
        """
        plain_text = "Hello, World!"
        password = "secretpassword"
        result = encrypt(plain_text, password)
        
        self.assertIsInstance(result, dict)
        self.assertIn('cipher_text', result)
        self.assertIn('salt', result)
        self.assertIn('iv', result)
        self.assertEqual(len(result['cipher_text']), 24)
        self.assertEqual(len(result['salt']), 24)
        self.assertEqual(len(result['iv']), 24)

    def test_decrypt(self):
        """
        Test the decrypt function.
        """
        enc_dict = {
            'cipher_text': 'qSRdiZzrZdbj2k7tSlI91w=='.encode('utf-8'),
            'salt': 'gE1siAoRH0qOjh3uC6id9Q=='.encode('utf-8'),
            'iv': '4y5QSrKvkd++LD2OoMAYHg=='.encode('utf-8')
        }
        password = "secretpassword"
        decrypted = decrypt(enc_dict, password)
        
        self.assertEqual(decrypted, "Hello, World!")

    def test_decrypt_wrong_password(self):
        """
        Test the decrypt function with wrong password.
        """
        enc_dict = {
            'cipher_text': 'qSRdiZzrZdbj2k7tSlI91w=='.encode('utf-8'),
            'salt': 'gE1siAoRH0qOjh3uC6id9Q=='.encode('utf-8'),
            'iv': '4y5QSrKvkd++LD2OoMAYHg=='.encode('utf-8')
        }
        password = "wrongpassword"
        decrypted = decrypt(enc_dict, password)

        self.assertEqual(decrypted, '')

    def test_encrypt_decrypt(self):
        """
        Test the encrypt and decrypt functions together.
        """
        plain_text = "Hello, World!"
        password = 'secretpassword'
        enc = encrypt(plain_text, password)
        dec = decrypt(enc, password)
        self.assertEqual(dec, plain_text)


if __name__ == '__main__':
    unittest.main()