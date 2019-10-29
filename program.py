import random

testBoard = ['a','X','O','X','O','X','O','X','O','X']

def displayBoard(board):
    index = 0
    for i in range(1,len(board)):
        print(board[i] , end = "  ")
        index += 1
        if index%3 == 0:
            print()
            print()
            index = 0 
        
def playerInput():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: Select your marker? Type X or O:    ").upper()
        if marker == 'X':
            return ('X','O')
        else:
            return ('O', 'X')

def placeMarker(board, position, marker):
    board[position] = marker

def checkIfWon(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or 
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or 
            (board[8] == mark and board[5] == mark and board[2] == mark) or 
            (board[9] == mark and board[6] == mark and board[3] == mark) or 
            (board[7] == mark and board[5] == mark and board[3] == mark) or 
            (board[9] == mark and board[5] == mark and board[1] == mark))

def chooseFirst():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def spaceCheck(board, position):
    return board[position] == ' '

def fullBoardCheck(board):
    for i in range(1,10):
        if spaceCheck(board, i):
            return False
    return True

def playerChoice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] and not spaceCheck(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

def replay():
    return input("Do you wanna play again? Yes or No").lower().startswith('y')

if __name__ == "__main__":
    while(True):
        playingBoard = [' '] * 10
        player1Marker, player2Marker = playerInput()
        turn = chooseFirst()
        print("{} will go first!!!!".format(turn))

        play = input("Are you ready to play? Y or N")
        if play[0].lower() == 'y':
            continuePlaying = True
        else:
            continuePlaying = False

        while(continuePlaying):
            if turn == 'Player 1':
                displayBoard(playingBoard)
                position = playerChoice(playingBoard)

                placeMarker(playingBoard, position, player1Marker)

                if checkIfWon(playingBoard, player1Marker):
                    displayBoard(playingBoard)
                    print("Player 1!!!!We have got our winner!!!! Congrats on your wonderful Victory")
                    continuePlaying = False
                else:
                    if fullBoardCheck(playingBoard):
                        displayBoard(playingBoard)
                        print("BOTH OF YOU COULD NOT WIN")
                        break
                    else:
                        turn = "Player 2"
            else:
                displayBoard(playingBoard)
                position = playerChoice(playingBoard)

                placeMarker(playingBoard, position, player2Marker)

                if checkIfWon(playingBoard, player1Marker):
                    displayBoard(playingBoard)
                    print("Player 2!!!! We have got our winner!!!! Congrats on your wonderful Victory")
                    continuePlaying = False
                else:
                    if fullBoardCheck(playingBoard):
                        displayBoard(playingBoard)
                        print("BOTH OF YOU COULD NOT WIN")
                        break
                    else:
                        turn = "Player 1"

        if not replay():
            break
