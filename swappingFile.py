def swapFileData():
    File1 = input("What is the name of file1 : ")
    File2 = input("What is the name of file2 : ")
    with open(File1, 'r') as a:
        dataA = a.read()
    with open(File2, 'r') as b:
        dataB = b.read()
    with open(File1, 'w') as a:
        a.write(dataB)
    with open(File2, 'w') as b:
        b.write(dataA)
    print("Successfully swapped")

swapFileData()