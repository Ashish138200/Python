import os
import shelve
import shutil
import send2trash #3rd party module
f = open('C:\\Users\\Ashish Chaurasia\\PycharmProjects\\AutomateBoringStuff\\venv\\MainCode\\Files\\hello.txt')
#print(f.read())
#f.readline()
content = f.read()
print(content)
f.close()
f1 = open('C:\\Users\\Ashish Chaurasia\\PycharmProjects\\AutomateBoringStuff\\venv\\MainCode\\Files\\hello1.txt', 'w')
f1.write("YOYO")
f1.close()
#----------------------------shelfFile----------------------------------------------------------------------------------
print("Shelf Files")
shelfFile = shelve.open('mydata') #creates binary file for storing data like dict., list and strings
shelfFile['cats'] = ['Zophie','Pooka','Simon','Fat-tail','Cleo']
print(shelfFile['cats'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
#-----------------------------------shutil------------------------------------------------------------------------------
print("Shutil")
# shutil.copy(location1,location2)
# shutil.copy(location1,location2\\newNameOfFile) for both copying and renaming
# shutil.copytree(location1,location2\\NewFolderName) for copying a whole folder and files
# shutil.move(location1,location2)
# shutil.move(location\\OldName,location\\NewName) for renaming
shutil.rmtree() #delete folder and all of its content

#------------------------------------OS Module--------------------------------------------------------------------------
print('OS')
os.getcwd()
os.sep()
# os.unlink(filename) # for deleting a file
os.rmdir() #for deleting a empty folder
'''for folderName,subfolderName, filenames in range os.walk('C:\\hello'):
    print("The folder is" + folderName)
    print("Subfoder "+ subfolderName )
    print("Files" +filenames)'''

#----------------------------------------Send2Trash---------------------------------------------------------------------
print('Send2Trash')
send2trash.send2trash(path='') # will delete the file and send it to recycle bin