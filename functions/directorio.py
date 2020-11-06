import os
import shutil

class directorio:
    
    def __init__(self, newdir = "", arcsel = "", nowdir=""):
        self.newdir = newdir
        self.arcsel = arcsel
        self.nowdir = nowdir
    
    def changedir(self):
        strnd = str(self.newdir)
        os.chdir(strnd)
    
    def showfile(self):
        n = os.listdir(path=self.nowdir)
        return n
        
    def copy(self):
        shutil.copy(self.arcsel,self.newdir)

    def move(self):
        shutil.move(self.arcsel,self.newdir)
