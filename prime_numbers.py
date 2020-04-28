'''
Prime Numbers:
this progam will generate and show next prime numbers untill user decides to stop.
The prime number is number that can be devided only by 1 and the number itself.
'''

print('Welcome!')
press_key = 'Press any key to start printing following prime numbers!\n'.center(100)
input(press_key)
num = 2
x = ''

while x.lower() != 'exit':
    for a in range(2, num):
        if num % a == 0:
            num += 1
    else:
        print(num, 'is a prime.')
        x = input('Press any key to continue or type "exit" to exit program... ')
        num += 1

print('Bye!')
