from random import shuffle

'''
    Choose the correct location of the ball
'''

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def insert(text=' '):
    return int(input(f"Pick a location of 1, 2, or 3{text}: "))

def user_guess(text = ' '):
    guess = ''
    guess = insert()

    while guess not in [1,2,3]:
        guess = insert(' again')

    return int(guess-1)

def check(mylist):
    lst = mylist
    guess = user_guess()

    if lst[guess] == 'O':
        print(lst)
        print('Correct')
    else:
        print('Wrong')
        check(lst)


# INITIAL LIST
mylist = [' ', 'O', ' ']

# SHUFFLED LIST
new_lst = shuffle_list(mylist)
print(new_lst)

# USER GUESS & CHECK GUESS
check(new_lst)

