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


def part1():
    data = getdata()
    counter = 0
    for segment in data:
        isvalid = analyse(segment)
        if isvalid == True:
            counter += 1
    return counter