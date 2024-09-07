import sys
sys.path.append('./')
from db.emoji import encode, decode
import unittest

class TestEmoji(unittest.TestCase):

    def test_encode(self):
        # Test with a single character
        assert encode('a') == '🤢'
        assert encode('b') == '👿'
        assert encode('c') == '👹'
        
        # Test with a word
        assert encode('hello') == '🤖💩🫦🫦👂'
        assert encode('world') == '🐔👂🤷🫦👺'
        
        # Test with special characters
        assert encode('!@#$%^&*()') == '!@#$%^&🎯()'
        
        # Test with empty string
        assert encode('') == ''
        
        # Test with mixed characters
        assert encode('a1b2c3') == '🤢🦥👿🌺👹🍇'

    def test_decode(self):
        # Test with a single character
        assert decode('🤢') == 'a'
        assert decode('👿') == 'b'
        assert decode('👹') == 'c'

        # Test with a word
        assert decode('🤖💩🫦🫦👂') == 'hello'
        assert decode('🐔👂🤷🫦👺') == 'world'

        # Test with special characters
        assert decode('!@#$%^&🎯()') == '!@#$%^&*()'

        # Test with empty string
        assert decode('') == ''

        # Test with mixed characters
        assert decode('🤢🦥👿🌺👹🍇') == 'a1b2c3'
    
    def test_encode_decode(self):
        # Test with a single character
        assert decode(encode('a')) == 'a'
        assert decode(encode('b')) == 'b'
        assert decode(encode('c')) == 'c'
        
        # Test with a word
        assert decode(encode('hello')) == 'hello'
        assert decode(encode('world')) == 'world'
        
        # Test with special characters
        assert decode(encode('!@#$%^&*()')) == '!@#$%^&*()'
        
        # Test with empty string
        assert decode(encode('')) == ''
        
        # Test with mixed characters
        assert decode(encode('a1b2c3')) == 'a1b2c3'

if __name__ == '__main__':
    unittest.main()