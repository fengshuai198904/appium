# encoding: utf-8
"""
Nuomi iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import inspect
import fnmatch as m
import paramunittest
import os
import sys 
sys.path.append("../..")

from random import randint
from appium import webdriver
import driver.appdriver as appdriver
import libs.common as lib
from time import sleep
import libs.operation as operation
global driver
driver = appdriver.AppDriver()
lib = lib.CommonClass()
operation = operation.Operation()


class Test(unittest.TestCase):
    """
    setUp
    """
    @classmethod
    def setUpClass(self):
        print 'setUpClass'
        global operationdriver
        operationdriver = driver.start_app_driver()

        operation.click(operationdriver, 'name', 'guide skip')

        operation.click(operationdriver, 'xpath', 
            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIAButton[2]')
        #mine
        operation.click(operationdriver, 'xpath', 
            '//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[4]')
        #login
        
        operation.click(operationdriver, 'xpath', 
            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIAButton[1]')
        operation.click(operationdriver, 'xpath', 
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[3]')
        operation.send_key(operationdriver, 'xpath', 
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIATextField[1]',
             0, '13917973631')
        operation.send_key(operationdriver, 'xpath', 
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIASecureTextField[1]',
             0, '19890407')
        operation.click(operationdriver, 'xpath', 
            '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAButton[1]')

    @classmethod
    def tearDownClass(self):
        driver.stop_app_driver()
        print 'tearDownClass'

    def setUp(self):
        print 'setup'
        print operation.get_context(operationdriver)
        if operation.get_context(operationdriver) != "NATIVE_APP":
            operationdriver.switch_to.context('NATIVE_APP')
        print operation.get_context(operationdriver)
        operation.click(operationdriver, 'xpath', 
            '//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[1]')

    def tearDown(self):
        print 'teardown'

    # def test_demo(self):
    #     self.assertTrue(1 == 1)

# if __name__ == '__main__':
#     print "test run_test_case is begin"
#     driver.run_test_case(self, os.path.join(lib.workspace(), 'case', lib.foldername()), Test)


