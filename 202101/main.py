

def solution():
    ip =  open("input.txt", "r").readlines()
    lastSeq = int(ip[0]) + int(ip[1]) + int(ip[2])
    counter = 0

    for i in range(1, 1998):
      currSeq = int(ip[i]) + int(ip[i + 1]) + int(ip[i + 2])

      if currSeq > lastSeq:
        counter += 1

      lastSeq = currSeq
     #print("current sequence: ", currSeq)

    print(counter)

if __name__ == '__main__':
    solution()
