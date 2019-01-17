#!/usr/python
import random
import time
 
def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
print()

def chooseCave():
    print('which cave will you go into? (1 or 2)')
    global cave
    cave = input()
    if cave == '1' or cave =='2':
        
     print('You approch the cave...')
     time.sleep(2)
     print('Its dark and spooky...')
     time.sleep(2)
     print('A large dragon jumps out in front of you he opens his jaws and.....')
     print()
     time.sleep(2)

     friendlyCave = random.randint(1,2)
  
     if cave ==str(friendlyCave):
        print('gives you his treasure')
     else:
        print('Gobbles you down in one bite')


playAgain = 'yes'
while playAgain == 'yes' or playAgain =='y':
    displayIntro()
    chooseCave()
    


    print('Do you want to play again?(Yes or NO)')
    playAgain =input()


    

