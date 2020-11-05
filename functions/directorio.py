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
        shutil.copy(src=f"{self.arcself}",dst=f"{self.newdir}")
        

    def move(self):
        shutil.move(source=f"{self.nowdir}\\{self.arcsel}",destination=f"{self.newdir}\\{self.arcsel}")



    


# change the current directory 
# to specified directory
#print(os.getcwd())
#os.chdir(r"C:\Users\Daniel\Documents") 
#print("Directory changed")
#print(os.=)
#nd = op3(r'C:\Users\Daniel\Documents')
#nd.changedir()
#op3.changedir()