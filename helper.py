def draw_board(spots):
    board = f'|{spots[1]}|{spots[2]}|{spots[3]}|\n|{spots[4]}|{spots[5]}|{spots[6]}|\n|{spots[7]}|{spots[8]}|{spots[9]}|'
    print(board)

def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'