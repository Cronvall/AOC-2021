import statistics

FILE = open("input.txt", 'r').read().split(',')
IP = []
for obj in FILE:
    IP.append(int(obj))
IP.sort()

def solution1():
    median = IP[int(len(IP) / 2)]

    fuelCost = 0
    for obj in IP:
        fuelCost += abs(obj - median)
    print(fuelCost)

def solution2(list, position):
    fueltot = 0
    for i in list:
        fueltot += sum(fuelcalc(abs(position - i)))
    result = fueltot, position
    return  result


#Used for Solution2
def fuelcalc(rng):
    sum_lst = []
    counter = 0
    for i in range(rng):
        counter += 1
        sum_lst.append(counter)
    return  sum_lst


#Used to solve Solution2 (Very diry way to do it)
def superDuperLoop():
    result =  solution2(IP, round(statistics.mean(IP)))
    for i in range(len(IP)):
        newSol = solution2(IP, i)
        if newSol[0] < result[0]:
            result = newSol
    return result


if __name__ == "__main__":
    solution1()
    print(superDuperLoop())