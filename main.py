import re
import os

names = set()
scriptFiles = []


def findVariableNames(file):
    with open(file, 'r') as f:
        contents = f.read()
    
    pattern = r"\((S\.L|L\.L)\.(\w+)\)"
    matches = re.findall(pattern, contents)
    variables = [match[1] for match in matches]

    return variables


def findScriptFiles(filePath):
    for root, dirs, files in os.walk(filePath):
        for file in files:
            if file.lower().endswith(".osc"):
                scriptFiles.append(os.path.join(root, file))

def modifyFileName(fileName):
    return fileName.replace(".osc", "_varlist.txt")

def processScriptFile(file, output):
    names.clear()
    try:
        for variable in findVariableNames(file):
            names.add(variable)
        with open(output, 'w') as varlist:
            for name in names:
                varlist.write(f"{name}\n")

    except FileNotFoundError:
        print(f"File '{file}' not found. Please check the file path.")

def main():
    findScriptFiles("")
    for scriptFile in scriptFiles:
        processScriptFile(scriptFile, modifyFileName(scriptFile))

if __name__ == "__main__":
    main()