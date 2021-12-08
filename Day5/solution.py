import numpy as np

def soltuion1():
    file = open("input.txt", 'r')
    map = np.zeros([1000, 1000])
    for line in file:
        line = line.split()
        x1, y1 = line[0].split(',')
        x2, y2 = line[2].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

        if x1 == x2:
            distance = range(min(y2,y1),max(y2,y1) +1)
            for y in distance:
                map[y][x1] += 1

        elif y1 == y2:
            distance = range(min(x2,x1), max(x2,x1)+1)
            for x in distance:
                map[y1][x] += 1

        else:
            if x1 < x2 or y1 < y2:
                distance_x = range(x1, x2)
                distance_y = range(y1, y2)
            elif x1 >= x2 or y1 >= y2:
                distance_x = range(x2, x1)
                distance_y = range(y2, y1)


            for diagonal, y in enumerate(distance_y):
                print(diagonal)
                map[distance_x[diagonal]][y] += 1
                print([y])
                print([distance_x[diagonal]])
                print(distance_x)



    counter =0
    for y in range(0,1000):
        for x in range(0,1000):
            if(map[y][x] >= 2):
                counter += 1

    print(counter)

if __name__ == "__main__":
    soltuion1()
