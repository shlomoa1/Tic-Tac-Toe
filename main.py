from helper import draw_board, check_turn
import os

# a dict for every spot on the board
spots = {1:'1', 2:'2', 3: '3', 4: '4', 5: '5',
          6: '6', 7: '7', 8: '8', 9: '9'}

playing = True
turn = 0

while playing:
    # clearing the termenal after every turn
    os.system('cls' if os.name == 'nt' else 'clear')
    # drawing the board using the helper file
    draw_board(spots)

    choice = input()
    if choice == 'q':
        playing = False

    turn +=1
    spots[int(choice)] = check_turn(turn)