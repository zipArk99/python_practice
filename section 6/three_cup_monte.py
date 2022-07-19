
from random import shuffle 


threeCups=['','o','']


def shuffle_the_cups():
    shuffle(threeCups)
    print('\n\n\n===cup shuffled===\n\n\n')
    choice2=int(raw_input('what do you think in which cup there is a ball 0, 1 or 2::'))
    print('\n\n')
    if(threeCups[choice2]=='o'):
        print('correct answer ball is in cup number:: {}'.format(choice2))
    else:
        print('sorry ball is not in cup number:: {}'.format(choice2))
        
    for index,value in enumerate(threeCups):
        print('cup[{num}]-->{value}'.format(num=index,value=value))
    


while True:
    print('\n\n-----1 to play game-----')
    print('-----2 to quit game----')
    choice=int(raw_input('Select any one option which are givn below::'))
    
    if(choice==1):
        shuffle_the_cups()
    elif(choice==2):
        break
    else:
        print('error please select appropriate option')

print("Thanks for playing the game see you again")