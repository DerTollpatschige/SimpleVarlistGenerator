from lib.libfile import LibFile

def main():
    filepath = input("Enter the Directory: ")

    libfile = LibFile(filepath, "varlist")
    libfile.findfiles()
    for file in libfile.getdirectorycontents():
        libfile.writeoutput(file)


if __name__ == "__main__":
    main()