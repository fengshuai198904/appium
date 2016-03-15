"""This is a docstring"""
import os
import signal
import sys
sys.path.append("..")
import urllib2
from multiprocessing import Process
import config.config as config
import libs.common as common
from appium import webdriver
import threading
import time
configLocal = config.ReadConfig()
lib = common.CommonClass()


class AppiumServer(object):
    """docstring for AppiumServer"""
    def __init__(self):
        global openAppium, baseUrl
        openAppium = configLocal.get_cmd_value("openAppium")
        baseUrl = configLocal.get_config_value("baseUrl")
        
    def is_running(self):
        """
        determine whether AppiumServer is running
        retrun:True or False
        """
        response =None
        url = baseUrl + '/status'

        try:
            time.sleep(3)
            response = urllib2.urlopen(url, timeout=10)
            
            if str(response.getcode()).startswith("2"):
                return True
            else:
                return False
        except urllib2.URLError as e:
            return False
        finally:
            if response:
                response.close()

    def start_server(self):
        """
        start the appium server 
        retrun:
        """
        print "begin start appium server"
        thread = RunServer(openAppium)
        p = Process(target=thread.start())
        p.start()
        time.sleep(2)
        if self.is_running():
            print "start_appium_server succcess"
        else:
            print "start_appium_server failue"
        
    def stop_server(self):
        """
        stop the appium server
        retrun:
        """
        print "begin stop appium server"
        try:
            time.sleep(2)
            lib.kill_process("node")
            #os.system('pkill node')
        except Exception as e:
            raise e
        else:
            pass
        finally:
            pass
        
        if self.is_running():
            print "stop_appium_server failue"
        else:
            print "stop_appium_server succcess"

    def re_start_server(self):
        """
        re_start_appium_server
        retrun:
        """
        self.stop_server()
        time.sleep(2)
        self.start_server()
        
        if self.is_running():
            print "re_start_appium_server succcess"
        else:
            print "re_start_appium_server failue"


class RunServer(threading.Thread):
    """
    docstring for RunServer
    """
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)

# if __name__ == '__main__':
#     appium_server = AppiumServer()
#     appium_server.re_start_server()
#     print appium_server.is_running()
#     appium_server.stop_server()
   

    
    

        

