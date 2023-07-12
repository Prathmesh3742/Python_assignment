def assign7(fname):
    try:
        f = open(fname,"+a")
    except FileExistsError:
        print("File does not exist exception")
    f.writelines("Roll no :36 \nName : Prathmesh \nClass : CO-A")
    f.seek(0)
    print(f.readlines())
    f.close()

assign7("assign7.txt")
