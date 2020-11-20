#!/usr/bin/python3
 
from random import randint
 
v = 'j'
while(v == 'j'):
    player = input('Sten (s),Påse (p), Sax (x))?')
    info = None
 
    if player == 's':
        info = 'Sten'
    elif player == 'p':
        info = 'Påse'
    elif player == 'x':
        info = 'Sax'
    else:
        info = 'Felaktigt val!'
    print(info, 'vs', end=' ')
 
    chosen = randint(1,3)
    #print(chosen)
    if chosen == 1:
        val = 'Sten'
        computer = 's'
    elif chosen == 2:
        val = 'Påse'
        computer = 'p'
    elif chosen == 3:
        val = 'Sax'
        computer = 'x'
    else:
        val = 'Felaktigt val Datorn'
 
    print(val)
 
    if player == computer:
        print('Oavgjort')
    elif player == 's' and computer == 'x':
        print('Spelaren vann!')
    elif player == 's' and computer == 'p':
        print('Datorn vann!')
    elif player == 'p' and computer == 's':
        print('Spelaren vann!')
    elif player == 'p' and computer == 'x':
        print('Datorn vann!')
    elif player == 'x' and computer == 'p':
        print('Spelaren vann!')
    elif player == 'x' and computer == 's':
        print('Datorn vann!')
     
    v = input ('Spela igen (j/n)')

   
 