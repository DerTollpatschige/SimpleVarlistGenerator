import os

def cleanFile(file):
    with open(file) as f:
        lines = f.readlines()
        uniqueSet = set(lines)

    with open(file, 'w') as f:
        f.writelines(uniqueSet)

def removeOverlappingContent(file1, file2):

    with open(file1, 'r') as f1:
        contentOfFile1 = set(f1.readlines())
    
    with open(file2, 'r') as f2:
        contentOfFile2 = set(f2.readlines())
    
    uniqueContent = contentOfFile1 - contentOfFile2

    with open (file1, 'w') as f1:
        f1.writelines(uniqueContent)
    

def findFiles(folderPath):
    files = [file for file in os.listdir(folderPath) if file.lower().endswith(".txt")]

    for file in files:
        filePath = os.path.join(folderPath, file)
        cleanFile(filePath)
        print(f"Duplicates removed from {file}")
    
    for i, file1 in enumerate(files):
        for j, file2 in enumerate(files):
            if i != j:
                removeOverlappingContent(os.path.join(folderPath, file1), os.path.join(folderPath, file2))
                print(f"Removed overlapping content between {file1} and {file2}")

def main():
    findFiles("")

if __name__ == "__main__":
    main()