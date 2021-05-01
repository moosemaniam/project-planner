import pickle
from project import project
from task import task
class app:
    project=None
    def __init__(self):
        self.project = None

    def CreateNewProject(self,projectname,projectCode):
        self.project = project(projectname,projectCode)

    def OpenProject(self,picklename):
        self.project=None
        with open(picklename,'rb') as file:
            self.project=pickle.load(file)

    def saveCurrentProject(self,picklename):
        with open(picklename,'wb') as file:
            pickle.dump(self.project,file)
    def printInfo(self):
        self.project.printinfo()

    def getInfo(self):
        return(self.project.getinfo())

    def printInfo(self):
        info = self.project.getinfo()
        return info

    """Delete a project"""
    def deleteProject(self):
        del(self.project)

    def createTask(self,
            taskname,
            engineer,
            startDate,
            effortInDays,
            dependentTasks
            ):
        if(self.project==None):
            return None
        T = task(taskname,engineer,startDate,EffortinDays,dependentTask)
        self.project.tasks.append(T)



