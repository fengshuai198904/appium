"""This is a docstring"""
import os
import sys
import signal

class CommonClass(object):
    """docstring for Common"""

    def workspace(self):
        """This is a docstring"""
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)

    def filename(self):
        """This is a docstring"""
        value = sys.argv[0][sys.argv[0].rfind(os.sep)+1:].split('.')
        return value[0]

    def kill_process(self, pstring):
        """This is a docstring"""
        for line in os.popen("ps ax | grep " + pstring + " | grep -v grep"):
            fields = line.split()
            pid = fields[0]
            os.kill(int(pid), signal.SIGKILL)
            print pstring, "shutdown is success"
    
    def foldername(self, path):
        """This is a docstring"""
        foldername = path.split('/')[len(path.split('/'))-1]
        return foldername
# if __name__ == '__main__':
#     test = CommonClass()
#     print test.workspace()
#     print test.filename()