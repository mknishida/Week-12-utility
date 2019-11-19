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

def UpdateString(string_1, string_2, index):
    print(string_1[:index] + string_2 + string_1[index+1:])
