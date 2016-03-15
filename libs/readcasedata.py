# -*- coding:utf-8 -*-
"""
Read Case From File and Generate Executable Test Case
"""

import os
import json
import operation
import sys
import getcasedata as getcasedata
import common as common
lib = common.CommonClass()

operation = operation.Operation()


class ReadCaseData(object):
    """docstring 
    for ReadCaseData
    """
    def read_from_file(self, casedata_path=None):

        """
        read_from_file
            """
        testmethod = []
        
        for parent, dirnames, filenames in os.walk(casedata_path):
            for filename in filenames:   
                casedatapath = os.path.join(parent, filename) 
                #print  casedatapath
                file = open(casedatapath, "r")
                for line in file:
                    case_json = json.loads(line)
                    if case_json['casename'] not in testmethod:
                        testmethod.append(case_json['casename'])
                        #print case_json['modularname']
                        testcasepath = os.path.join(lib.workspace(), 'case', 
                            case_json['modularname'], 'test' + case_json['modularname'] + '.py')
                        #print testcasepath
                        casefile = open(testcasepath, 'a')
                        casefile.write("\n")
                        casefile.write("\n" + "    def " + case_json['casename'] + '(self):')
                
                    try:
                        casefile.write("\n")
                        if case_json['op'] == 'click':
                            
                            casefile.write("        " + 'operation.click(operationdriver, "'
                                + case_json['targetType'] + '", "' + case_json['target'] + '")')

                        elif case_json['op'] == 'text':
                            
                            casefile.write("        " + 'operation.send_key(operationdriver, "'
                                + case_json['targetType'] + '", "' + case_json['target'] + '", 0 ,"'
                                + case_json['targetInput'] + '")')

                        elif case_json['op'] == 'tap':
                            
                            casefile.write("        " + 'operation.tap(operationdriver, "' 
                                + case_json['targetType'] + '", "' + case_json['target'] +'")')


                        elif case_json['op'] == 'assertDisplay':
                            
                            casefile.write("        " + 'operation.is_exist(operationdriver, "' 
                                + case_json['targetType'] + '", "' + case_json['target'] +'")')
                  

                        elif case_json['op'] == 'assertTrue':
                            
                            casefile.write("        " + 'operation.is_exist(operationdriver, "'
                                + case_json['targetType'] + '", "' + case_json['target'] +'")')

                        elif case_json['op'] == 'assertEqual':
                            
                            casefile.write("        " + 'operation.is_exist(operationdriver, "'
                                + case_json['targetType'] + '", "' + case_json['target'] +'")')

                        elif case_json['op'] == 'scroll':
                            if case_json['direction'] == 'up':
                                
                                casefile.write("        " + 'operation.swipe_to_up()')
                            elif case_json['direction'] == 'down':
                                casefile.write("        " + 'operation.swipe_to_down()')
                     
                            elif case_json['direction'] == 'left':
                                casefile.write("        " + 'operation.swipe_to_left()')
                           
                            elif case_json['direction'] == 'right':
                                casefile.write("        " + 'operation.swipe_to_right()')

                    except:
                        pass
                                
                casefile.close()
                file.close()


if __name__ == '__main__':
    #getcase = getcasedata.parser_params()
    test = ReadCaseData()
    test.read_from_file(os.path.join(lib.workspace(), 'data'))