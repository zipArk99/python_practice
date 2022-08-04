import unittest
import file1


class TestFile1(unittest.TestCase):
    
    def test_case_1(self):
        text='Python'
        result=file1.capitalize_text(text)
        self.assertEqual(result,text)
         
    def test_case_2(self):
        text='Hey Python'
        result=file1.capitalize_text(text)
        self.assertEqual(result,text)
        
        
        
if __name__ == '__main__':
    unittest.main()
    
        