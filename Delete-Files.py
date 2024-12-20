#Batch Delete V1.0.3

#This program was made to batch delete files but also be universal in doing so. It is still a work in progress with a few more added features to come.
#It currently does not delete a folder within a folder and that is the next feature being worked on.
import os

#all of the print statements that print a variable are meant for testing what the variable is pulling/displaying

class Test:
    def __init__(self):
        #Designate the path
        self.dirPath = input('Input path: ')
        os.chdir(self.dirPath)
        self.dirList = [item for item in os.listdir(self.dirPath) if os.path.isdir(os.path.join(self.dirPath, item))]
        'print(self.dirList)'
        self.dirPath2 = {}
        for item in self.dirList:
           self.dirPath2[item] = os.path.join(self.dirPath, item)
        'print(self.dirPath2)'
        self.listPath2 = list(self.dirPath2.values())
        'print(self.listPath2[0])'

        #select if it is a file or a folder
        self.delType = input('File or Folder?: ')
        
        #skipping people
        self.skipNum = input('How many folders would you like to skip?: ')
        self.skipList = []
        for n in range(int(self.skipNum)):
            self.name = input('Name of Folder to skip: ')
            self.namePath = os.path.join(self.dirPath, self.name)
            self.skipList.append(self.namePath)
        'print(self.skipList[0])'

        #file code
        if self.delType.lower() == 'file':
            self.fileName = input('Input file name: ')

            #Enter Desired File Name
            if os.path.exists(self.fileName):
                os.remove(self.fileName)
            else:
                print('File does not exist')
        
        #folder code
        elif self.delType.lower() == 'folder':
            self.folderName = input('Input folder name: ')
            #go through each folder indivdually
            for i in range(len(self.listPath2)):
                if self.listPath2[i] not in self.skipList:
                    self.dirPath3 = self.listPath2[i] + "\\" + self.folderName
                    #delete each file indivdually
                    if os.path.exists(self.dirPath3):
                        self.inside = [f for f in os.listdir(self.dirPath3) if os.path.isfile(os.path.join(self.dirPath3, f))]
                        for j in range(len(self.inside)):
                            os.chdir(self.dirPath3)
                            self.delFile = os.path.join(self.dirPath3, self.inside[j])
                            'print(self.delFile)'
                            os.remove(self.delFile)
                        os.chdir(self.listPath2[i])
                        os.rmdir(self.dirPath3)
                        print(os.path.basename(self.listPath2[i]) + ': Done')
                    else:
                        print(os.path.basename(self.listPath2[i]) + ': Folder does not exist')
                else:
                    print(os.path.basename(self.listPath2[i]) + ': Skipped')
        #confirm program end
        print('Deletion Completed')
    
test_instance = Test()    

#Created by Justin Cordero and Spencer Albrecht, 2024