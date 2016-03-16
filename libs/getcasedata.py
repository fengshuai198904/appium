# -*- coding:utf-8 -*-
# !/usr/bin/env python
################################################################################
#
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
This module is the log module Baidu.com supplies
author
"""

import urllib2
import json
import sys
import os
import shutil
import common as common
lib = common.CommonClass()


def get_requester(url):
    """get方式
    """
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read().decode('utf-8')
    json_str = json.loads(res)
    return json_str


def parser_params():
    """调用autoinfo接口，过滤接口返回结果，并将有用数据写入test.txt文件
    """
    url = "http://xxxxxxxxxxxxxxxxs/openplatform/autoxtime/autoinfo?osname=ios"
    data = get_requester(url)
    casecontentdata = []
    casetestmodularnamedata = []
    casenamedata = []
    
    if(not data['errno']):
        for item in data['data']['list']:
            for k, v in item.items():
                # if k == 'casecontent':
                #     casecontentdata.append(v)
                if ((k == 'testmodularname') and (v not in casetestmodularnamedata)):
                    casetestmodularnamedata.append(v)
                # if k == 'casename':
                #     casenamedata.append(v)

    if(os.path.exists(os.path.join(lib.workspace(), 'data'))):
        shutil.rmtree(os.path.join(lib.workspace(), 'data'))
 
    if(os.path.exists(os.path.join(lib.workspace(), 'case'))):
        shutil.rmtree(os.path.join(lib.workspace(), 'case'))


    if(casetestmodularnamedata != []):
        for datadir in casetestmodularnamedata:
            print datadir
            if(not os.path.exists(os.path.join(lib.workspace(), 'data', datadir))):
                os.makedirs(os.path.join(lib.workspace(), 'data', datadir))

            if(not os.path.exists(os.path.join(lib.workspace(), 'case', datadir))):
                os.makedirs(os.path.join(lib.workspace(), 'case', datadir))
                caseinitpath = os.path.join(lib.workspace(), 'case', datadir)
                casetestdemopath = os.path.join(lib.workspace(), 'case', datadir, 'test' + datadir + '.py')
                initpath = os.path.join(lib.workspace(), '__init__.py')
                testdemopath = os.path.join(lib.workspace(), 'testdemo.py')
                shutil.copy(initpath, caseinitpath)
                shutil.copy(testdemopath, casetestdemopath)

            datapath = os.path.join(lib.workspace(), 'data', datadir, 'test' + datadir + '.txt')
            outputfile = open(datapath, 'w')
            if(not data['errno']):
                for item in data['data']['list']:
                    if (item['testmodularname'] == datadir):
                        #print item['casecontent']

                        for i in json.loads(item['casecontent']):
                        
                            outputfile.write('{"modularname":"' + datadir + '","casename":"' + item['casename'] + '",')
                            outputfile.write('"op":"' + i['op'] + '",')
                            outputfile.write('"target":"' + i['opcontent']['target'].encode('utf-8') + '",')

                            if i['op'] == 'click':
                                outputfile.write('"targetType":"' + i['opcontent']['targetType'] + '"}\n')

                            elif i['op'] == 'scroll':
                                outputfile.write('"targetType":"' + i['opcontent']['targetType'] + '",')
                                outputfile.write('"direction":"' + i['opcontent']['direction'] + '"}\n')

                            elif i['op'] == 'assertEqual':
                                outputfile.write('"targetType":"' + i['opcontent']['targetType'] + '"}\n')

                            elif i['op'] == 'assertNotEqual':
                                outputfile.write('"targetType":"' + i['opcontent']['targetType'] + '"}\n')

                            elif i['op'] == 'assertTrue':
                                outputfile.write('"targetType":"' + i['opcontent']['targetType'] + '"}\n')

                            elif i['op'] == 'assertFalse':
                                outputfile.write('"targetType":"' + i['opcontent']['targetType'] + '"}\n')

                            elif i['op'] == 'text':
                                outputfile.write('"targetType":"' + i['opcontent']['targetType'] + '",')
                                outputfile.write('"targetInput":"' + i['opcontent']['targetInput'] + '"}\n')

                            elif i['op'] == 'assertDisplay':
                                outputfile.write('"targetType":"' + i['opcontent']['targetType'] + '"}\n')

                            elif i['op'] == 'assertNotDisplay':
                                outputfile.write('"targetType":"' + i['opcontent']['targetType'] + '"}\n')
                                 
            outputfile.close()
  


def get_id():
    """调用
    """
    url = "http://xxxxxxxxxxxxxxxxxxxxx/openplatform/autoxtime/autotestsuite?\
            casename=264"
    data = get_requester(url)
    print data

# if __name__ == "__main__":
    
#     parser_params()