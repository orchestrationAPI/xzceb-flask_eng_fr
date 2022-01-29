
import os
import unittest
from translator import english_to_french , french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french('Hello'),'Bonjour') 
        self.assertNotEqual(english_to_french(" "), " ") 
        self.assertNotEqual(french_to_english(" "), " ")  
        self.assertNotEqual(french_to_english('Bonjour'),'Hello')

unittest.main()        
        