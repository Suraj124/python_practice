import capital_every_letter
import unittest

class Text_capital_every_letter(unittest.TestCase):

    def one_word_text(self):
        text="python"
        res=capital_every_letter.cap(text)
        print(res)
        self.assertEqual(res,'Python')
    
    def mul_word_text(self):
        text='python programmin'
        res=capital_every_letter.cap(text)
        print(res)
        self.assertEqual(res,'Python programming')
if __name__=='__main__':
    unittest.main()
