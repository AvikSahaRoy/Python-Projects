from random import randint

user_pass = input('Enter your password: ')
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
guess = ''
count = 0
while(guess != user_pass):
    guess = ''
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, 25)]
        guess = str(guess_letter) + str(guess)
        print(guess)
        count += 1
print('Your password is: ',guess)
print(count)