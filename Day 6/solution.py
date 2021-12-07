import numpy as np

FILE = open("input.txt", 'r').read().split(',')
def solution1(days):
    fish = []
    for ch in FILE:
        fish.append(int(ch))

    for i in range(0, days):
        for x in range(0, len(fish)):
            fish[x] -= 1
            if fish[x] < 0:
                fish[x] = 6
                fish.append(8)

    print(len(fish))

def get_fish():
    fish = np.array([int(x) for x in FILE])
    ret_val = np.zeros((9,), dtype=np.longlong)
    for i in range(9):
        ret_val[i] = np.count_nonzero(fish == i)
    return ret_val

def solution2(days):
    fish = get_fish()
    for i in range(days):
        reproducing_fish = fish[0]
        fish[0:8] = fish[1:9]
        fish[6] += reproducing_fish
        fish[8] = reproducing_fish

    print(fish.sum())

if __name__ == "__main__":
    solution1(80)
    solution2(80)
    solution2(256)
