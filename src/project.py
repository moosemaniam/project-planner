from task import task
from engineer import engineer
class project:

    tasks = []
    engineers = []
    def __init__(self,name,projectcode):
        self.name = name
        self.projectcode = projectcode
        self.startDate=None
        self.customer=None

    def printinfo(self):
        print(self.name,self.projectcode,self.tasks,self.engineers)

    def getinfo(self):
        return("NAME:" + str(self.name) + \
        str(self.projectcode)+str(self.tasks),self.engineers)

