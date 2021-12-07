
FILE = open("input.txt", 'r').read().split(',')


def solution1():
    ip = []
    for obj in FILE:
        ip.append(int(obj))
    ip.sort()
    median = ip[int(len(ip) / 2)]

    fuelCost = 0
    for obj in ip:
        fuelCost += abs(obj - median)
    print(fuelCost)


def solution2():
    #TODO
    pass



if __name__ == "__main__":
    solution2()