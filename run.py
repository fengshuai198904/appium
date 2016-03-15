# encoding: utf-8
"""
 run.py-ci
"""
import os
import sys 
import re
global evnconfig
evnconfig = len(sys.path)
import config.config as readConfig
import unittest
import driver.appdriver  as appdriver
import libs.common 
from time import sleep
import libs.HTMLTestRunner as report
import urllib2
import time
import shutil
global driver, caselist, switch, testcasefilenames
readConfig= readConfig.ReadConfig()
caselist = readConfig.get_config_value("caselist")
switch = readConfig.get_config_value("switch")
lib = libs.common.CommonClass()
casePath = os.path.join(lib.workspace(), 'case')
driver = appdriver.AppDriver()





class Alltest(object):
    """
    Alltest
    """
    def driver_on(self):
        """open the driver
        :return:
        """
        print 'setUpClass'
        driver.start_app_driver()

    def driver_off(self):
        """close the driver
        :return:
        """
        driver.stop_app_driver()
        print 'tearDownClass'

    def set_case_list(self):
        """from the caseList get the caseName,set in caseList
        :return:
        三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        """
        caseData=  [[] for i in range(2)]
        for parent, dirnames, filenames in os.walk(casePath):  

            for dirname in  dirnames:
                if int(switch)==1 and dirname in caselist:
                    caseData[0].append(dirname)
                    for nextparent, nextdirnames, nextfilenames in os.walk(os.path.join(casePath, dirname)):
                        casenum = len(dirnames)>len(nextfilenames) and len(dirnames) or len(nextfilenames)   
                        for nextfilename in nextfilenames:
                            caseData[1].append(nextfilename)
                else:
                    caseData[0].append(dirname)
                    for nextparent, nextdirnames, nextfilenames in os.walk(os.path.join(casePath, dirname)):
                        casenum = len(dirnames)>len(nextfilenames) and len(dirnames) or len(nextfilenames)   
                        for nextfilename in nextfilenames:
                            caseData[1].append(nextfilename)

            return caseData

    def create_suite(self):
        """from the caseList,get caseName,According to the caseName to search the testSuite
        :return:test_suite
        """
        case_list = self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module_list = []
        if len(case_list[1]) > 0:

            for case_folder in case_list[0]:
                casePath = os.path.join(lib.workspace(), 'case', case_folder + '/')
                case_module = 'test' + case_folder
                case_files = case_module + '.py' 
                sys.path.remove(sys.path[0])
                sys.path.insert(0, casePath)
                files = os.listdir(casePath)                               
                test = re.compile('^test', re.IGNORECASE) 
                files = filter(test.search, files) 
                test1 = re.compile('\.py$', re.IGNORECASE)  
                files = filter(test1.search, files) 

                filenameToModuleName = lambda f: os.path.splitext(f)[0]

                moduleNames = map(filenameToModuleName, files)         
                modules = map(__import__, moduleNames)                 
                load = unittest.defaultTestLoader.loadTestsFromModule  
                unittests = unittest.TestSuite(map(load, modules)) 
                suite_module_list.append(unittests) 

                while len(sys.path)!= evnconfig:
                    sys.path.pop()
                    pass
 
        if len(suite_module_list) > 0:
            for suite in suite_module_list:
                for test_name in suite:
                    test_suite.addTest(test_name)

        else:
            return None
        return test_suite

    def run(self):
        """run test
        :return:
        """
        try:
            suite = self.create_suite()
            if suite is not None:

                foldername = time.strftime('%Y%m%d%H%M%S', time.localtime())
                os.makedirs(os.path.join(lib.workspace(), 'output/case', foldername))
                pathdir = os.path.join(lib.workspace(), 'output/case', foldername, 'report.html')
                fp = open(pathdir, 'wb')

                runner = report.HTMLTestRunner(stream=fp, title='testReport', description='Report_description')
                runner.run(suite)
                fp.close()
                reportpwd = os.path.join(lib.workspace(), 'output/', 'report.html')
                shutil.copy(pathdir, reportpwd)


            else:
                print  "Have no test to run"
        except Exception as ex:
            print ex

if __name__ == "__main__":

    test = Alltest()
    test.run()


