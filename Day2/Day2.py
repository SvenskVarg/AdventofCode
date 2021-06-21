def getdata():
     f = open("Day2/input")
     text = f.read().split("\n")
     list = [element.split(" ") for element in text]
     return list

def analyse(segment):
    datarange = segment[0]
    letter = segment[1][0]
    password = segment[2]
    occurence = 0
    for l in password:
        if l == letter:
            occurence += 1
    minmax = datarange.split("-")
    min = int(minmax[0])
    max = int(minmax[1])
    if occurence >= min and occurence <= max:
        return True
    else:
        return False

def interpret(part):
    datarange = part[0]
    letter = part[1][0]
    password = part[2]
    occurences = 0
    firstlast = datarange.split("-")
    first = int(firstlast[0])
    last = int(firstlast[1])
    pass1 = password[first]
    pass2 = password[last]
    if pass1 == letter:
        occurences += 1
    if pass2 == letter:
        occurences += 1






def part1():
    data = getdata()
    counter = 0
    for segment in data:
        isvalid = analyse(segment)
        if isvalid == True:
            counter += 1
    return counter

def part2():
    data = getdata()
    counter = 0
    for part in data:
        isvalid = interpret(part)
