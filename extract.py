# module imports
import zipfile
import os
import subprocess
import sys

# set the current working folder
path = "./"
args = sys.argv

# -------------------------------------------- private methods
def getFolders(folderPath):
    foldersList = []
    # get list of all files / folders in path
    entities = os.listdir(folderPath)
    # get list of only the folders
    for entity in entities:
        if os.path.isdir(folderPath + entity):
            foldersList.append(entity)

    return foldersList

# -------------------------------------------- main method
def main():
    print("\033[0;31m","EXTRACTOR -> Project Extractor v1.0 - Sean Morrow [Apr 2023]")

    # get list of all student folders downloaded for project from brightspace
    studentfolders = getFolders(path)
    print(studentfolders)

    # go through each folder and extract the zip file inside it
    for studentFolder in studentfolders:
        zipFile = ""
        # find name of zip file (should only be one)
        for file in os.listdir(path + studentFolder):
            if file.endswith(".zip"):
                zipFile = file
                break
        
        # test if no zip file was found in folder
        if zipFile == "":
            print("\033[0;31m","EXTRACTOR -> No zip file found in folder: " + studentFolder)
            continue

        # get the path to the zip file in student's folder
        zipFilePath = path + studentFolder + "/"

        print("\033[0;32m","EXTRACTOR -> extracting : " + zipFilePath + zipFile)

        # extract the zip file
        with zipfile.ZipFile(zipFilePath + zipFile, 'r') as zip_ref:
            zip_ref.extractall(zipFilePath)

            # do npm install if specified in arguments
            # if len(args) > 1 and (args[1] == "-npm" or args[1] == "-n"):
            # get project folder extracted from zip file (should only be one)
            projectFolders = getFolders(zipFilePath)
            # run npm install on each extracted folder
            for projectFolder in projectFolders:
                print("\033[0;33m","EXTRACTOR -> running npm install in: " + projectFolder)
                p = subprocess.Popen(["npm", "i"], cwd=zipFilePath + projectFolder, shell=True)
                p.wait()

    print("EXTRACTOR -> project extraction complete")

main()