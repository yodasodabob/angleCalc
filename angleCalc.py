from scipy import *

class rocket:
    def __init__(self, filePath):
        with open(filePath, 'r') as keyFile:
            contents = keyFile.read().split
            print contents
            self.name = contents[0].split(' ')[2:]




def angleCalc(rocketFile, conditionsFile, distance):
    print('Do Stuff')
