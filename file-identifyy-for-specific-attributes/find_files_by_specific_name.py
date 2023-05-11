import os
#os.chdir("find-files-with-specific-attributes")
path1 = os.getcwd()

# Function: Display all files and folders names under the specified path
def findName(path):
    fullPathList = []

    for dirPath, dirNames, fileNames in os.walk(path):
        for name in fileNames:
            fullPathList.append([name, dirPath + '\\' + name])

    for fileNames, fullPath in fullPathList:
        #print(fileNames, fullPath)
        if '10MB' in fileNames:
            src = fullPath    # Move file: source location
            des = path + '\\' + fileNames    # Move file: target location
            #print(src, des)
            os.rename(src, des)    # Move file
            print("File moved successfully:", src, "->", des)    # Show file moved successfully

if __name__ == '__main__':
    findName(path1)