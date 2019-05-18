from os import getcwd,chdir,listdir

print(getcwd())   #current working directory

chdir('../')    #back to one directory
print(getcwd())

chdir('./File_Handling')
print(getcwd())

print(listdir(getcwd()))    #list all files and folder of current working directories

