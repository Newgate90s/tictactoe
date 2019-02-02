# Starts here
# init vars
# init board
board = [' ' for x in range(10)]

# The board layout
def board_print(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

# If position is ' ', it's free
def free(pos):
    return board[pos] == ' '

# Letter and position is the label
def label(letter, pos):
    board[pos] = letter

# Defines the AI move, the move will be random choice
def ai_move():
    free_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in free_moves:
            board_copy = board[:]
            board_copy[i] = let
            if winner(board_copy, let):
                move = i
                return move

    free_corners = []
    for i in free_moves:
        if i in [1, 3, 7, 9]:
            free_corners.append(i)

    if len(free_corners) > 0:
        move = random_choice(free_corners)
        return move

    if 5 in free_moves:
        move = 5
        return move

    free_sides = []
    for i in free_moves:
        if i in [2, 4, 6, 8]:
            free_sides.append(i)

    if len(free_sides) > 0:
        move = random_choice(free_sides)

    return move

# Defines human move, move will be player input
def human_move():
    run = True
    while run:
        move = input('Place your X on the board. Select 1-9: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if free(move):
                    run = False
                    label('X', move)
                else:
                    print('Position taken.')
            else:
                print('Number outside of range.')
        except:
            print('Only numbers are accepted.')

# Defines how random choice works
def random_choice(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

# If there is 0 ' ' positions, board is full
def full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

# All possible ways to win
def winner(bo, la):
    return (bo[7] == la and bo[8] == la and bo[9] == la) or (bo[4] == la and bo[5] == la and bo[6] == la) or (
            bo[1] == la and bo[2] == la and bo[3] == la) or (bo[1] == la and bo[4] == la and bo[7] == la) or (
                   bo[2] == la and bo[5] == la and bo[8] == la) or (
                   bo[3] == la and bo[6] == la and bo[9] == la) or (
                   bo[1] == la and bo[5] == la and bo[9] == la) or (bo[3] == la and bo[5] == la and bo[7] == la)

# Asks the player if they want to start by asking for an input
def start_game():
    answer = input('\nStart the game? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        # board = [' ' for x in range(10)]
        print('-----------------------------------')
        print('-----------------------------------')
        print('-----------------------------------')
    else:
        print("Leaving imulation, have a nice day!")

# Askk the player if they want to play again by asking for an input
def play_again():
    answer = input('\nPlay again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        # board = [' ' for x in range(10)]
        print('-----------------------------------')
        print('-----------------------------------')
        print('-----------------------------------')
        main()
    else:
        print("Leaving simulation, have a nice day!")

def main():
    # Prints an introduction, rules and an example board to help the user understand position numbers
    print('Welcome to Human vs AI Tic Tac Toe')
    print('\nRules: Pick 1-9 to try and get three X in a line')
    print('\nBoard: ')
    print('   |   |  ')
    print('' + board[1] + '1 | 2' + board[2] + '| 3' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |  ')
    print('' + board[4] + '4 | 5' + board[5] + '| 6' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   | ')
    print('' + board[7] + '7 | 8' + board[8] + '| 9' + board[9])
    print('   |   |')
    start_game()

    print('\nGame Starts!')
    print('AI goes first.\n\n')

    # While the board still has a place to move
    while not (full(board)):

        # If Human 'x' has not won, the let AI move.
        if not (winner(board, 'X')):
            # Get Move from AI
            move = ai_move()
            # Evaluate AI move
            if move == 0:
                # Board is full after AI moved
                print('Tie game!')
            else:
                # Put AI 'o' move on the board
                label('O', move)
                print('AI placed an O on ', move, ':')
                board_print(board)
        else:
            # Human 'X' has already won! AI does not get a move.
            print('Human player wins!')
            break
            # If AI 'o' has not won, then let human move
        if not (winner(board, 'O')):
            # Get human move here
            human_move()
            # Print out board after human has moved.
            board_print(board)
        else:
            # AI 'o' has won the game, game over!
            print('AI wins!')
            break
    # If board is full and no there is no winner, game is a tie
    if full(board):
        print('Tie game!')
    # Runs play again function which asks player if they want to play again
    play_again()


# Program starts here
# Go to main game loop
main()






