
# Configuration global variables

easy_board_template = """
 {_1_} | {_2_} | {_3_}
"""

medium_board_template = """
 {_1_} | {_2_} | {_3_}
-----------
 {_4_} | {_5_} | {_6_}
 """

hard_board_template = """
  {_1_} | {_2_} | {_3_}
 -----------
  {_4_} | {_5_} | {_6_}
 -----------
  {_7_} | {_8_} | {_9_}
  """

welcome_message = """
Welcome to A to Z memory trainer! Let's strengthen your memory!
"""

board_select_message = """
Please pick a game difficulty by typing a number: 3 (easy), 6 (medium), or 9 (hard).
"""

play_question = """
Would you like to play a game? Type "y" for yes and "n" for no.
"""

input_question = """
Pick the {} spot.
"""

invalid_input_response = """
Please pick an open spot on the board by typing a number.
"""

easy_win_statement = """
You got all three right! Maybe you should try medium!
"""

medium_win_statement = """
You got all six right! Maybe you should try hard!
"""

hard_win_statement = """
You got all nine right! You are the memory master!
"""

easy_lose_statement = """
You can't even remember three things? You're such a fucking loser. Here's the right answer:
"""

medium_lose_statement = """
No that wasn't right. Here's the right answer:
"""

hard_lose_statement = """
No that wasn't right. Here's the right answer:
"""

exit_statement = """
Thanks for playing!
"""

# Global game state variables

current_board_easy = [
    'A', 'B', 'C'
]

current_board_medium = [
    'A', 'B', 'C'
    'D', 'E', 'F'
]

current_board_hard = [
    'A', 'B', 'C'
    'D', 'E', 'F'
    'G', 'H', 'I'
]

current_turn = 1

current_game_state = 'initialize'

valid_choices_easy = ['1', '2', '3']
valid_choices_medium = ['1', '2', '3', '4', '5', '6']
valid_choices_hard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Global functions

def clear_screen():
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")

def draw_board_easy(board=None, template = easy_board_template):
    """
        Draws the easy game board. Can take params to draw dynamically. By default it uses the global game state variables.
    """

    global current_board_easy
    if board is None:
        board = current_board_easy

    gb = template.format(
    _1_ = board[0],
    _2_ = board[1],
    _3_ = board[2]
    )

    clear_screen()
    print(gb)
    print('\n'*5)

def draw_board_medium(board=None, template = medium_board_template):
    """
        Draws the medium game board. Can take params to draw dynamically. By default it uses the global game state variables.
    """

    global current_board_medium
    if board is None:
        board = current_board_medium

    gb = template.format(
    _1_ = board[0],
    _2_ = board[1],
    _3_ = board[2],
    _4_ = board[3],
    _5_ = board[4],
    _6_ = board[5],
    )

    clear_screen()
    print(gb)
    print('\n'*5)

def draw_board_hard(board=None, template = hard_board_template):
    """
        Draws the medium game board. Can take params to draw dynamically. By default it uses the global game state variables.
    """

    global current_board_hard
    if board is None:
        board = current_board_hard

    gb = template.format(
    _1_ = board[0],
    _2_ = board[1],
    _3_ = board[2],
    _4_ = board[3],
    _5_ = board[4],
    _6_ = board[5],
    _7_ = board[6],
    _8_ = board[7],
    _9_ = board[8],
    )
