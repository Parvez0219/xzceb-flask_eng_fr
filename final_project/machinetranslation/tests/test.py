import unittest
import os
import sys
sys.path.insert(1, '/home/project/xzceb-flask-eng-fr/final_project/machinetranslation/')
from translator import english_to_french as englishToFrench,french_to_english as frenchToEnglish

class TestTranslation(unittest.TestCase):

    def test_englishToFrench_with_hello(self):
        self.assertEqual(englishToFrench('Hello'), {'translations': [{'translation': 'Bonjour'}], 'word_count': 1, 'character_count': 5})

    def test_englishToFrench_with_null_input(self):
        self.assertEqual(englishToFrench(None), {'translations': [{'translation': ''}], 'word_count': 0, 'character_count': 0})

    def test_frenchToEnglish_with_bonjour(self):
        self.assertEqual(frenchToEnglish('Bonjour'), {'translations': [{'translation': 'Hello'}], 'word_count': 1, 'character_count': 7})

    def test_frenchToEnglish_with_null_input(self):
        self.assertEqual(frenchToEnglish(None), {'translations': [{'translation': ''}], 'word_count': 0, 'character_count': 0})

    def test_englishToFrench_with_bonjour(self):
        self.assertEqual(englishToFrench('Bonjour'), {'translations': [{'translation': 'Hello'}], 'word_count': 1, 'character_count': 7})

    def test_frenchToEnglish_with_hello(self):
        self.assertEqual(frenchToEnglish('Hello'), {'translations': [{'translation': 'Bonjour'}], 'word_count': 1, 'character_count': 5})

if __name__ == '__main__':
    unittest.main()