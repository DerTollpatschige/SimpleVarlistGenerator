import re
import os

names = set()
scriptFiles = []

def collectVariableNames(line, names):
    loadPattern = r"\d+\s+\(L\.L\.(.*?)\)"
    storePattern = r"\d+\s+\(S\.L\.(.*?)\)"

    loadMatch = re.search(loadPattern, line)
    storeMatch = re.search(storePattern, line)

    if loadMatch:
        varname = loadMatch.group(1)
    elif storeMatch:
        varname = storeMatch.group(1)
    else:
        return None
    
    if varname and varname not in names:
        names.add(varname)
        return varname
    return None

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
        with open(file, 'r', encoding='cp1252') as file:
            for line in file:
                varname = collectVariableNames(line, names)
                if varname:
                    names.add(varname)

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