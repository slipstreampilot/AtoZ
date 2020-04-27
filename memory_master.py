# imported modules
import random
import time

# global configuration variables

board_template = """
                        {_1_} | {_2_} | {_3_}
                        -----------
                        {_4_} | {_5_} | {_6_}
 """

welcome_message = """
******************************************************
******     Welcome to GREG'S MEMORY MASTER!    *******
******************************************************
*                                                    *
*****************    INSTRUCTIONS   ******************
*                                                    *
*  I'm going to show you a board with six letters.   *
*  You'll have 10 seconds to memorize the locations  *
*  of the letters (A, B, C, D, E, F) on the board.   *
*  Then, I'm going to show you a new board with the  *
*  numbers (1, 2, 3, 4, 5, 6). Your job is to input  *
*  the numbers one at a time that correctly          *
*  correspond to the ordered letter location. The    *
*  first number you type should be A's location.     *
*  The second number you type should be B's          *
*  location... and so on until you type all six.     *
*                                                    *
******************************************************

"""

win_message = """
******************************************************
*                                                    *
* You got them all right! You are the memory master! *
*                                                    *
******************************************************

"""

continue_message = "            Want to play again? (y/n) \n"

lose_message = """
\n
******************************************************
*                                                    *
*     You missed one. You need to practice more.     *
*                                                    *
******************************************************

"""

turn_message = "Pick the next number for the correct letter: "

ready_message = """
Press y followed by enter when you're ready to play!
\n                           """

# global game state variables

ordered_abc_list = ['A','B','C','D','E','F']

rand_abc_list = []

num_list = list(range(1,7))

current_game_state = 'initialize'

counter = 0

#main functions
def randomizer(list_a):
    """
    Takes a list and returns that list randomized. Also removes all list items from the original list.
    TODO: Don't destroy the original list?
    """
    list_b = list_a
    randomized_list = []
    for i in list(range(len(list_a))):
        selection = random.choice(list_b)
        index1 = list_b.index(selection)
        randomized_list.append(list_b.pop(index1))
    return randomized_list

def get_continue_choice():
    have_valid_choice = False

    while have_valid_choice == False:
        choice = input(continue_message)

        if choice == 'y' or choice == 'n':
            have_valid_choice = True
        else:
            print('The only valid inputs are y or n')

    return choice

def get_player_choice():
    have_valid_choice = False
    options = ['1', '2', '3', '4', '5', '6']

    while have_valid_choice == False:

        choice = input(turn_message)

        if choice in options:
            have_valid_choice = True
            options.pop(options.index(choice))
            print(options)

        else:
            print('The only valid inputs are the numbers left on the board')

    return int(choice)

def visible_countdown(t):
    while t > 0:
        print("                           " + str(t))
        print('\n')
        t -= 1
        time.sleep(1)

def invisible_countdown(t):
    while t > 0:
        t -= 1
        time.sleep(1)

def ready_to_play():
    have_valid_choice = False

    while have_valid_choice == False:
        choice = input(ready_message)

        if choice == 'y':
            have_valid_choice = True
        else:
            print('The only valid input is y')

    return choice

def reset_game():
    """
    Resets the game, producing a new randomized list of letters and a clear board
    """

    global ordered_abc_list
    global rand_abc_list
    global num_list
    global current_game_state
    global counter
    global board_template


    ordered_abc_list = ['A','B','C','D','E','F']
    rand_abc_list = randomizer(ordered_abc_list)
    ordered_abc_list = ['A','B','C','D','E','F']

    num_list = list(range(1,7))

    current_game_state = 'initialize'

    counter = 0

    board_template = """
                       {_1_} | {_2_} | {_3_}
                       -----------
                       {_4_} | {_5_} | {_6_}
                 """

    print('\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ')
    print(welcome_message)

    play_choice = ready_to_play()

    if play_choice == 'y':
        visible_countdown(5)

    print(board_template.format(
        _1_ = str(rand_abc_list[0]),
        _2_ = str(rand_abc_list[1]),
        _3_ = str(rand_abc_list[2]),
        _4_ = str(rand_abc_list[3]),
        _5_ = str(rand_abc_list[4]),
        _6_ = str(rand_abc_list[5])
        ))

    invisible_countdown(5)
    visible_countdown(5)

    print('\n \n \n \n \n \n \n \n \n \n \n \n \n \n ')

    print(board_template.format(
        _1_ = str(num_list[0]),
        _2_ = str(num_list[1]),
        _3_ = str(num_list[2]),
        _4_ = str(num_list[3]),
        _5_ = str(num_list[4]),
        _6_ = str(num_list[5])
        ))

def game_loop():
    """

    """

    global ordered_abc_list
    global rand_abc_list
    global num_list
    global current_game_state
    global counter

    while current_game_state != 'exit':

        reset_game()

        current_game_state = 'playing'

        while current_game_state == 'playing':
            while counter < len(num_list):
                user_input = get_player_choice()
                board = num_list
                location = board.index(user_input)
                board[location] = rand_abc_list[location]
                if rand_abc_list[location] == ordered_abc_list[counter]:

                    print('\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ')

                    print(board_template.format(
                    _1_ = str(board[0]),
                    _2_ = str(board[1]),
                    _3_ = str(board[2]),
                    _4_ = str(board[3]),
                    _5_ = str(board[4]),
                    _6_ = str(board[5])
                    ))
                    counter += 1
                else:
                    print(lose_message)
                    continue_choice = get_continue_choice()
                    if continue_choice == 'y':
                        current_game_state = 'initialize'
                        reset_game()
                    else:
                        exit()

            print(win_message)
            continue_choice = get_continue_choice()
            if continue_choice == 'y':
                current_game_state = 'initialize'
            else:
                exit()

#runs the program

game_loop()
