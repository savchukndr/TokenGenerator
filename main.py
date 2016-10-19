from tokenGen import Generator

print("This is a program for generating tokens.")
print()
while True:
    inpCount = input("Please, input amount of tokens:")
    inpCountTest = input("Please, input amount of \"testXX\" tokens:")
    if not (inpCount.isdigit() and inpCountTest.isdigit()):
        print("Not digit")
    else:
        gener = Generator(int(inpCount), int(inpCountTest))
        gener.lstToken()
        gener.readFile()
    ending = input("Make new file?(Y/N)")
    if ending == "Y" or ending == "y":
        print()
        continue
    elif ending == "N" or ending == "n":
        break
    else:
        print("\"{0}\" - its mean you want to continue!".format(ending))
        print()
        continue