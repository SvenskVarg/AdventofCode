def readdata():
    f = open("Day1/input.txt")
    text = f.read().split("\n")
    for l in range(0, len(text)):
        text[l] = int(text[l])
    return text

def part1():
    data = readdata()
    for l in data:
        for k in data:
            if l+k == 2020:
                return l*k


def part2():
    data = readdata()
    for l in data:
        for k in data:
            for j in data:
                if l+k+j == 2020:
                    return l*k*j

