import random
answer = random.randint(1, 10)
times = 3
print('----------made by yaokun----------')
temp = input('Please guess the number that 1-10:')
while temp.isdigit():
    temp = input('please enter a number that from 1 to 10')
guess = int(temp)
while times != 0:
    if guess == answer:
        print('What amazing!You just guessed the right number!')
    else:











