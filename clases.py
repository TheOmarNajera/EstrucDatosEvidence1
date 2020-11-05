import os
import shutil

class ops:
    
    def __init__(self, newdir = "", arcsel = ""):
        self.newdir = newdir
        self.arcsel = arcsel
    
    def changedir(self):
        strnd = str(self.newdir)
        if self.newdir == os.getcwd():
            print("Esta tratando de ir al directorio donde se encuentra actualmente")
        elif self.newdir != os.getcwd():
            print(f"El directorio '{os.getcwd()}' cambiará a '{self.newdir}'\n")
            os.chdir(strnd)
            print("\nEl directorio cambio correctamente. \n")
            print(f"\n el directorio actual es: {os.getcwd()}")
    
    def selectfile(self):
        print(f"usted se encuentra actualmente en {os.getcwd()}")
        for raiz, dirs, archivos in os.walk(".", topdown=True):    #Demostración de unpacking
            n = archivos    
        con = 0
        for a in n:
            con += 1
            print(f"{con}: {a}")
        sf = input("\n Seleccione un archivo de la anterior lista")
    
    def copy(self):
        shutil.copy(f"{arcsel},{newdir}")
        print(f"¡El archivo '{arcsel}' se ha movido a '{newdir}' exitosamente!")

    def move(self):
        shutil.move(f"{arcsel},{newdir}")
    


# change the current directory 
# to specified directory
#print(os.getcwd())
#os.chdir(r"C:\Users\Daniel\Documents") 
#print("Directory changed")
#print(os.=)
#nd = op3(r'C:\Users\Daniel\Documents')
#nd.changedir()
#op3.changedir()