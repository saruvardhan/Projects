import random as rn
cards = (11,2,3,4,5,6,7,8,9,10,10,10,10)
com = ['hit','stand']
player = rn.sample(cards,2)
print(f'you deck of number is {player}')
extra_card=input("Do you want to hit a card or stand: ").lower()
print(f'you chose: {extra_card}')
if extra_card == 'hit':
    n1 = rn.sample(cards,1)
    player.append(n1[0])
    print(f'your cards are {player}')    
computer = rn.sample(cards,2)
print(f'the computer chose {computer}')
cc=rn.sample(com,1)
print(f'computer chose:{cc}')
if cc ==['hit']:
    n1 = rn.sample(cards,1)
    computer.append(n1[0])
    print(computer)
add1=0
add2=0
for i in player:   
    add1+=i  
print(f'your total is {add1}')    
for x in computer:
    add2+=x
print(f'computers total is {add2}')    
if add1 >21:
    print('you lose :(')
    print ('computer win')
elif add2>21:
    print('you win :)')
elif add1 > add2:
    print('you win :)')
elif add1 == add2:
    print('draw')
else:
    print('you lose')

 
    
