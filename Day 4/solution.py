import re


def main():
    numbers = list()
    file = open("input.txt", 'r')
    board_output = make_board(5, file, list())
    #board_output = [(0)numbers on board, (1)all boards]
    bingo_search(5, board_output[0], board_output[1])


def make_board(col_length, file, boards):
    numbers = []
    read_input = [re.split(' +|,', line.strip()) for line in file]

    for row in read_input:
        if (row == read_input[0]): #Handles the row of drawings
            numbers = [num for num in row]
        elif (row == ['']): #When empty row add the board
            boards.append(list())

        elif(len(row) == col_length): #Add row to board
            boards[len(boards) - 1].extend([i for i in row])

    return numbers, boards

def bingo_search(col_length, numbers,boards):
    numWins = 0
    for num in numbers:
        for board in (board for board in boards):
            try:
                board[board.index(num)] = ""
                for i in range(0, col_length):

                    row_empty = "".join(board[i::col_length]) == ""
                    col_empty = "".join(board[i * col_length:][:col_length]) == ""

                    if row_empty or col_empty:
                        if numWins == 0:
                            print("Solution 1: ", int(num) * sum(int(i) if i.isnumeric() else 0 for i in board))
                        elif numWins == len(boards) -1:
                            print("Solution 2: ", int(num) * sum(int(i) if i.isnumeric() else 0 for i in board))
                        numWins += 1
                        board.clear()
                        break
            except:
                pass

if __name__ == '__main__':
    main()