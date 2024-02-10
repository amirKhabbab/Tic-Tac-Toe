
def printBoard(player1,player2):
    one = 'X' if player1[0]==1 else '0' if player2[0]==1 else 1
    two = 'X' if player1[1]==1 else '0' if player2[1]==1 else 2
    three = 'X' if player1[2]==1 else '0' if player2[2]==1 else 3
    four = 'X' if player1[3]==1 else '0' if player2[3]==1 else 4
    five = 'X' if player1[4]==1 else '0' if player2[4]==1 else 5
    six = 'X' if player1[5]==1 else '0' if player2[5]==1 else 6
    seven = 'X' if player1[6]==1 else '0' if player2[6]==1 else 7
    eight = 'X' if player1[7]==1 else '0' if player2[7]==1 else 8
    nine = 'X' if player1[8]==1 else '0' if player2[8]==1 else 9
    print(f"{one} | {two} | {three}")
    print(f"--|---|--")
    print(f"{four} | {five} | {six}")
    print(f"--|---|--")
    print(f"{seven} | {eight} | {nine}")

# def checkDraw(player1,player2):
#     sum=0
#     for i in range(9):
#         sum+=player1[i]+player2[2]
#     if sum==9:
#         return 1
#     return 0


def checkWin(player1,player2):
    wins =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,4,9],[3,5,7]]

    for win in wins:
        if player1[win[0]-1]+player1[win[1]-1]+player1[win[2]-1]==3:
            print("---------------")
            print("Player1[X] Win!!")
            print("---------------")
            return 1
        if player2[win[0]-1]+player2[win[1]-1]+player2[win[2]-1]==3:
            print("---------------")
            print("Player2[0] Win!!")
            print("---------------")
            return 2
    return 0


if __name__ == "__main__":
    print("-----------------------------")
    print(" Welcome to Tic Tac Toe game ")
    print("-----------------------------\n")
    player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    turn = 1
    printBoard(player1,player2)
    while(True):
        if turn==1:
            print("\n")
            print("Player1's[X] Chance!!")
            value = int(input("Please enter the cell no.: "))
            if player1[value-1]!=0 or player2[value-1]!=0:
                print("\nCell already occupied! Try again.")
                turn = 0
            else:
               player1[value-1] = 1
        else:
            print("\n")
            print("Player2's[0] Chance!!")
            value = int(input("Please enter the cell no.: "))
            if player1[value-1]!=0 or player2[value-1]!=0:
                print("\nCell already occupied! Try again.")
                turn = 1

            else:
               player2[value-1] = 1
            
        print("\n")
        printBoard(player1,player2)
        check = checkWin(player1,player2)
        # draw = checkDraw(player1,player2)
        if check!=0:
            break
        # if draw==1:
        #     print("Draw the match")

        turn = 1-turn
            
    

