from tokenGen import Generator

print("This is a program for generating tokens.")
print()
inpCount = input("Please, input amount of tokens:")
inpCountTest = input("Please, input amount of \"testXX\" tokens:")
if not (inpCount.isdigit() and inpCountTest.isdigit()):
    print("Not digit")
else:
    gener = Generator(int(inpCount), int(inpCountTest))
    gener.lstToken()
    gener.readFile()