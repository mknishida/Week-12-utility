#
#Morgan Nishida
#CSCI 102 - B
#Week 12 - Part A

def PrintOutput(string):
    print('OUTPUT ',string)

def LoadFile(file):
    f = open(file,"r")
    lines = f.readlines()
    print("OUTPUT" ,lines)
