from email.base64mime import body_encode


board=[[1,2,3],[4,5,6],[7,8,9]]
player_chance=True
player_wins=False


def is_box_empty(row,column):
    if(board[row,column] not in ['X','O']):
        return True
    else:
        return False
    

def print_board():
    
    print('\n\n')
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
    print('\n\n')
    

def check_empty_space():
    for row in range(0,len(board)):
        for column in range(0,len(board)):
            if(board[row][column] not in ['X','O']):
                return True         
    else:False
    
       
def check_player_turn():
    global player_chance
    return 'X' if player_chance else 'O'


def mark_board(input):
    index=0
    if(input in [1,2,3]):
        index = board[0].index(input)
        if(not is_box_empty(0,index)):
            return False
        board[0][index] = check_player_turn()
    elif(input in [4,5,6]):
        index = board[1].index(input)
        if(not is_box_empty(1, index)):
            return False
        board[1][index]=check_player_turn()
    elif(input in [7,8,9]):
        index = board[2].index(input)
        if(not is_box_empty(2, index)):
            return False
        board[2][index] =check_player_turn()
    return True

   
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
    
    print('{}'.format('PLAYER 1::X' if check_player_turn() else 'PLAYER 2::0'))

    user_input=int(raw_input("Select any available number from the board player {player}::"
                             .format(player=check_player_turn())))
    if(mark_board(user_input)):
        print('Already filled place please select another place player {}'.format(check_player_turn()))
        continue
    check_winner()
    if(player_wins):
        print_board()
        break
    
