from lib2to3.pgen2 import driver
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\paulv\Desktop\sele\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)

    def test_hello (self):
        driver = self.driver
        driver.get('http://www.platzi.com')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello-world-report')    )
