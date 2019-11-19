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

def FindWordCount(input_list,string):
    count = 0
    for i in input_list:
        if string in i:
            count += 1
    print('OUTPUT ',count)

def ScoreFinder(names,scores,player):
    lower_names = []
    for name in names:
        lower = name.lower()
        lower_names.append(lower)
    if player in names:
        index = names.index(player)
        print('OUTPUT ',player,'got a score of',scores[index])
    elif player in lower_names:
        cap_name = player.capitalize()
        index = lower_names.index(player)
        print('OUTPUT ',cap_name,'got a score of',scores[index])
    else:
        print('OUTPUT player not found')

def Union(list_1,list_2):
    for i in list_1:
        if i in list_2:
            list_2.remove(i)
    print('OUTPUT ',list_1 + list_2)

def Intersection(list_1,list_2):
    intersection = []
    for i in list_1:
        if i in list_2:
            intersection.append(i)
    print('OUTPUT ',intersection)
