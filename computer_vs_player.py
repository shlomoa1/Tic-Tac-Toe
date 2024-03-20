
import os
import random
import time

# Define the player symbols
PLAYER_X = 'X'
PLAYER_O = 'O'

# Define winning combinations
WIN_COMBINATIONS = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),
    (1, 4, 7), (2, 5, 8), (3, 6, 9),
    (1, 5, 9), (3, 5, 7)
]

# Helper function to draw the Tic Tac Toe board
def draw_board(spots):
    board = f'|{spots[1] if spots[1] != " " else 1}|{spots[2] if spots[2] != " " else 2}|{spots[3] if spots[3] != " " else 3}|\n|{spots[4] if spots[4] != " " else 4}|{spots[5] if spots[5] != " " else 5}|{spots[6] if spots[6] != " " else 6}|\n|{spots[7] if spots[7] != " " else 7}|{spots[8] if spots[8] != " " else 8}|{spots[9] if spots[9] != " " else 9}|'
    print(board)


# Helper function to check for a win
def check_for_win(spots, player):
    for combo in WIN_COMBINATIONS:
        if spots[combo[0]] == spots[combo[1]] == spots[combo[2]] == player:
            return True
    return False

# Helper function to check for a tie
def check_for_tie(spots):
    return ' ' not in spots.values()

# Function to generate the computer's move with the specified logic
def get_computer_move(spots, player):
    opponent = PLAYER_X if player == PLAYER_O else PLAYER_O
    
    # Check for immediate win opportunities
    for spot in spots:
        if spots[spot] == ' ':
            spots[spot] = player
            if check_for_win(spots, player):
                return spot
            spots[spot] = ' '
    
    # Check for immediate blocking opportunities
    for spot in spots:
        if spots[spot] == ' ':
            spots[spot] = opponent
            if check_for_win(spots, opponent):
                return spot
            spots[spot] = ' '
    
    # If there's no immediate threat, prioritize certain spots based on the specified logic
    prioritized_spots = [5, 1, 3, 7, 9, 2, 4, 6, 8]
    for spot in prioritized_spots:
        if spots[spot] == ' ':
            return spot
    
    # If all else fails, make a random move
    available_spots = [spot for spot in spots if spots[spot] == ' ']
    return random.choice(available_spots)

# Initialize the game
spots = {i: ' ' for i in range(1, 10)}
playing = True
turn = 0

# Main game loop
while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    # Player's turn
    if turn % 2 == 0:
        print("Player's turn: pick your spot (1-9) or press q to quit.")
        choice = input()
        if choice == 'q':
            playing = False
        elif str.isdigit(choice) and int(choice) in spots and spots[int(choice)] == ' ':
            spots[int(choice)] = PLAYER_X
            turn += 1
        else:
            print("Invalid choice! Please choose a valid spot.")
            time.sleep(2)  # Wait for 2 seconds before continuing
    # Computer's turn
    else:
        print("Computer's turn:")
        choice = get_computer_move(spots, PLAYER_O)
        spots[choice] = PLAYER_O
        turn += 1
    
    # Check for win or tie
    if check_for_win(spots, PLAYER_X):
        playing = False
    elif check_for_win(spots, PLAYER_O):
        playing= False
    elif check_for_tie(spots):
        playing = False

# Print final board and result
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

if check_for_win(spots, PLAYER_X):
    print('Player wins!')
elif check_for_win(spots, PLAYER_O):
    print('Computer wins!')
else:
    print('It\'s a tie!')
