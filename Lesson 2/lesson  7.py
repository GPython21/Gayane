f = input("dfile.txt")
    print("dfile.txt", "r")


try:
    with open("dfile.txt") as f:
        print("dfile.txt")
except IOError:
    print('File is not present')