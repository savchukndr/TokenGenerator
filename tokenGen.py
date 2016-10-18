import random
import string


class Generator:
    def __init__(self, count):
        self.listToken = []
        if count.isdigit():
            self.count = count
        else:
            print(count, " Not Digit")

    @staticmethod
    def genToken():
        s = ''
        for x in range(13):
            s += random.choice(string.ascii_letters + string.digits)
        return s.lower()

    def lstToken(self):
        for x in range(1, int(self.count) + 1):
            s = str(self.genToken()) + '\n'
            self.listToken.append(s)
            self.listToken = list(set(self.listToken))
        for x in range(1, 21):
            s1 = "test" + str(x) + '\n'
            self.listToken.append(s1)

    def printList(self):
        for x in range(len(self.listToken)):
            print('{0}: {1}'.format(x, self.listToken[x]))

    @staticmethod
    def writeFileCSV(self):
        with open('randToken.csv', 'w') as f:
            for x in self.listToken:
                f.write(s)
            f.close()

    def readFile(self):
        self.writeFileCSV(self)
        with open('randToken.csv') as f:
            count1 = 0
            for line in f:
                count1 += 1
                print('{0}: {1}'.format(count1, f.readline()))
            f.close()


if __name__ == "__main__":
    I1 = Generator("1000")
    I1.lstToken()
    I1.printList()