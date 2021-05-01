from datetime import datetime
from engineer import engineer
class task:
    def __init__(self,name):
     self.name=name
     def __init__(self, name, engineer, taskID, dependentTaskID, startDate, EffortInDays):
        self.name=name
        self.assignedTo = engineer
        self.taskID = taskID
        self.dependentTask = dependentTask
        self.startDate = startDate
        self.EffortInDays= EffortinDays

     def addEngineer(self,engineer):
         self.assignedTo = engineer
     def assigntaskID(self,taskID):
         self.taskID = taskID
     def addDependentTask(self,dependentTask):
         self.dependentTask = dependentTask
     def addStartDate(self,startDate):
         self.startDate = startDate
     def addEffortInDays(self,EffortinDays):
         self.EffortInDays= EffortinDays
