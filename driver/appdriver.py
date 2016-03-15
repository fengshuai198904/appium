"""This is a docstring"""
import os
import sys
sys.path.append("..")
from selenium.common.exceptions import WebDriverException
import threading
from appium import webdriver
import urllib2 
import config.config as readConfig
configLocal = readConfig.ReadConfig()
import unittest
from random import randint
from appium import webdriver
from time import sleep
import libs.common as common
common = common.CommonClass()
import time
import libs.HTMLTestRunner as lib
import  appiumserver 
appiumserver = appiumserver.AppiumServer()

class AppDriver(object):
    """This is a docstring"""
    driver = None
    mutex = threading.Lock()
    workspace = readConfig.workspace
    platformName = configLocal.get_config_value("platformName")
    platformVersion = configLocal.get_config_value('platformVersion')
    deviceName = configLocal.get_config_value('deviceName')
    app = os.path.abspath(os.path.join(workspace, configLocal.get_config_value('appPath')))
    bundleId = configLocal.get_config_value('bundleId')
    baseUrl = configLocal.get_config_value('baseUrl')
    desired_capabilities = {
        'app': app,
        'platformName':platformName,
        'platformVersion':platformVersion,
        'deviceName':deviceName,
        'bundleId':"", 
        'locationServicesAuthorized':"true", 
        'autoAcceptAlerts':"true"

    }
 
    def start_app_driver(self):
        """This is a docstring"""
        try:
            
            
            while not appiumserver.is_running():
                appiumserver.re_start_server()
                sleep(1)
            else:
                if self.driver is None:
                    self.mutex.acquire()
                    try:
                        print "begin start AppDriver"
                        self.driver = webdriver.Remote(self.baseUrl, self.desired_capabilities)
                        print "start AppDriver success"
                    except urllib2.URLError as e:
                        self.driver = None
                        print e
                    self.mutex.release()

                return self.driver
        except WebDriverException:
            raise e

    def stop_app_driver(self):
        """This is a docstring"""
        if self.driver is None:
            return True
        else:
            print "begin stop AppDriver"
            self.driver.quit()
            print "stop AppDriver success"
            appiumserver.stop_server()

    def run_test_case(self, folder, TestClass=None):
        """This is a docstring"""
        suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)

        # unittest.TextTestRunner(verbosity=2).run(suite)
        #path = os.path.join(common.workspace(), 'output', 'report.html')
        foldername = time.strftime('%Y%m%d%H%M%S', time.localtime())
        os.makedirs(os.path.join(common.workspace(), 'output/case', folder, foldername))
        pathdir = os.path.join(common.workspace(), 'output/case', folder, foldername, 'report.html')
        fp = open(pathdir, 'wb')

        runner = lib.HTMLTestRunner(stream=fp, title='testReport', description='Report_description')
        runner.run(suite)
        fp.close()

# if __name__ == '__main__':
#     test = AppDriver()
#     test.start_app_driver()
#     test.stop_app_driver()
