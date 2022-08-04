import os
board=[[1,2,3],[4,5,6],[7,8,9]]
player_chance=True
player_wins=False

def get_box_location(input):
    
    for row in range(0,len(board)):
        for column in range(0,len(board)):
            if board[row][column] == input:
                return (row,column,True)
    return (row,column,False)
            
    
def is_box_empty(row,column):
    if(board[row,column] not in ['X','O']):
        return True
    else:
        return False
    

def print_board():

    print('\n')
    print('   {}  | {} |  {}   '.format(
        board[0][0], board[0][1], board[0][2]))
    print('      |   |      ')
    print('------|---|------')
    print('   {}  | {} |  {}   '.format(
        board[1][0], board[1][1], board[1][2]))
    print('------|---|------')
    print('      |   |      ')
    print('   {}  | {} |  {}   '.format(
        board[2][0], board[2][1], board[2][2]))
    print('\n')
    

def check_empty_space():
    for row in range(0,len(board)):
        for column in range(0,len(board)):
            if(board[row][column] not in ['X','O']):
                return True         
    else:False
    
       
def check_player_turn():
    global player_chance
    return 'X' if player_chance else 'O'


def mark_board(row,column):
    board[row][column]=check_player_turn()

   
def check_winner():
    global player_chance
    global player_wins
    for i in range(0,len(board)):
        if((board[i][0]==board[i][1] and board[i][1]==board[i][2]) or 
           (board[0][i]==board[1][i] and board[1][i]==board[2][i])):
            player_wins=True
            
    if((board[0][0]==board[1][1] and board[1][1]==board[2][2]) or 
       (board[0][2]==board[1][1] and board[1][1]==board[2][0])):
        player_wins=True
    
    else:
        player_chance=not player_chance
    
    
while True:

    print_board()
    if not check_empty_space():
        print('------ITS A TIE------')
        break
   
    if(check_player_turn()=='X'):
        print('PLAYER 1::X')
    else:
        print('PLAYER 2::O')
    user_input=int(raw_input("Select any available number from the board player {player}::"
                             .format(player=check_player_turn())))
    if(user_input in range(1,10)):
        location=get_box_location(user_input)
        if(location[2]==True):
            mark_board(location[0],location[1])
        else:
            os.system('clear')
            print("\n\n---Box {} is already filled please select another box---".format(user_input))
            continue
        check_winner()
        
        if(player_wins):
            os.system('clear')
            print_board()
            print('-----Congrulation player {} wins the game-----'.format(check_player_turn()))
            break
        os.system('clear')
    else:
        print('\n\n-----Please Select appropriate number between 1 to 9-----')
        continue
    
