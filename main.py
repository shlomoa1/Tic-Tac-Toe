from helper import draw_board , check_turn
import os

# a dict for every spot on the board
spots = {1:'1', 2:'2', 3: '3', 4: '4', 5: '5',
          6: '6', 7: '7', 8: '8', 9: '9'}

playing = True
turn = 0
prev_turn = -1

while playing:
    # clearing the termenal after every turn
    os.system('cls' if os.name == 'nt' else 'clear')

    # drawing the board using the helper file
    draw_board(spots)

    if prev_turn == turn:
        print('Invalid input or spot selected, please try again.')
    prev_turn = turn
    print('Player ' + str((turn % 2)+1)+"'s turn: pick your spot or press q to quit.")

    choice = input()
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {'X', 'O'}:
            turn +=1
            spots[int(choice)] = check_turn(turn)