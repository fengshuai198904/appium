"""This is a docstring"""
import os
import sys
sys.path.append("..")
import ConfigParser
import codecs 
import libs.common as common
global configfile_path, workspace

lib = common.CommonClass()
workspace = lib.workspace()
configfile_path = os.path.join(lib.workspace(), 'config/config.ini')
# print configfile_path,

class ReadConfig(object):
    """docstring for ReadConfig"""
    def __init__(self):
    
        fp = open(configfile_path)
        data = fp.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file =  codecs.open(configfile_path, "w")
            file.write(data)
            file.close()
        fp.close()

        self.cf = ConfigParser.ConfigParser()
        self.cf.read(configfile_path)

    def get_config_value(self, name):
        """This is a docstring"""       
        value = self.cf.get("config", name)
        return value

    def get_cmd_value(self, name):
        """This is a docstring"""
        value = self.cf.get("cmd", name)
        return value

# if __name__ == '__main__':
#     test = ReadConfig()
#     test.__init__()
#     print test.get_config_value('appPath')
#     print test.get_cmd_value('openAppium')




