import unittest
from app import app
class TestStringMethods(unittest.TestCase):

    def test_create_project(self):
        AppInstance=app()
        projectname="test123"
        projectCode=253424
        AppInstance.CreateNewProject(projectname,projectCode)
        AppInstance.printInfo()
        info = AppInstance.getInfo()
        self.assertEqual(info, NAME:test123253424[]', []")
    def test_open(self):
        AppInstance=app()
        projectname="Imagepipeline"
        projectCode=29143
        AppInstance.CreateNewProject(projectname,projectCode)
        previnfo = AppInstance.getInfo()
        AppInstance.saveCurrentProject("ISP.project")
        AppInstance.deleteProject()
        AppInstance.OpenProject("ISP.project")
        info = AppInstance.getInfo()
        self.assertEqual(info, previnfo)

if __name__ == '__main__':
    unittest.main()

