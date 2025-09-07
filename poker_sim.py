import random
from collections import Counter
import time

numbers= ("two","three","four","five","six","seven","eight","nine","ten","jack","king","queen","ace")
digits=(2,3,4,5,6,7,8,9,10,11,12,13,14)
suits=("spades","clubs","hearts","diamonds")



deck=[]




for suit in suits:
    for number in numbers:
        deck.append(number+' of '+suit)



hand1=random.sample(deck,k=1)
for card in hand1:    
    parts = card.split(" of ")
    num=parts[0]
    hand1v=digits[numbers.index(num)]
    hand1s=parts[1]
    deck.remove(card)

hand2=random.sample(deck,k=1)
for card in hand2:    
    parts = card.split(" of ")
    num=parts[0]
    hand2v=digits[numbers.index(num)]
    hand2s=parts[1]
    deck.remove(card)

bot1=random.sample(deck,k=1)
for card in bot1:    
    parts = card.split(" of ")
    num=parts[0]
    bot1v=digits[numbers.index(num)]
    bot1s=parts[1]
    deck.remove(card)

bot2=random.sample(deck,k=1)
for card in bot2:    
    parts = card.split(" of ")
    num=parts[0]
    bot2v=digits[numbers.index(num)]
    bot2s=parts[1]
    deck.remove(card)

flop1=random.sample(deck,k=1)
for card in flop1:    
    parts = card.split(" of ")
    num=parts[0]
    flop1v=digits[numbers.index(num)]
    flop1s=parts[1]
    deck.remove(card)

flop2=random.sample(deck,k=1)
for card in flop2:    
    parts = card.split(" of ")
    num=parts[0]
    flop2v=digits[numbers.index(num)]
    flop2s=parts[1]
    deck.remove(card)

flop3=random.sample(deck,k=1)
for card in flop3:    
    parts = card.split(" of ")
    num=parts[0]
    flop3v=digits[numbers.index(num)]
    flop3s=parts[1]
    deck.remove(card)

turn=random.sample(deck,k=1)
for card in turn:    
    parts = card.split(" of ")
    num=parts[0]
    turnv=digits[numbers.index(num)]
    turns=parts[1]
    deck.remove(card)

river=random.sample(deck,k=1)
for card in river:    
    parts = card.split(" of ")
    num=parts[0]
    riverv=digits[numbers.index(num)]
    rivers=parts[1]
    deck.remove(card)
   
money=10000
pot=0
opp_bet=0
pot=0

print(f'money:{money}')
print()
print()
print("Your hand:")
print()
print()
print(hand1)
print(hand2)
print()
print()
while True:
    
    user_input=input("What action would you like to take?(check,bet,fold)")
    if user_input=="fold":
        print("you have folded")
        exit()
    elif user_input=="bet":
        
        bet1=input('how much would you like to bet?')

        while True:
            if bet1.isnumeric() :
                bet=int(bet1)
                money=money-bet
                pot=pot+bet+bet
                print("Bot1 calls")
                print(f"current pot:{pot}")
                break
                
            else:
                print("Roman's a bum")
                time.sleep(0.1)

        break
    elif user_input=='check':
        print("Bot 1 checks")
        break
    else:
        print("yes, I did put in fail safes.")

print(f"money:{money}")
print()
print()
print(f"Current pot:{pot}")
print("Flop:")
print(flop1)
print(flop2)
print(flop3)
print()
print()

while 1==1:
    user_input=input("What action would you like to take?(check,bet,fold)")
    if user_input=="fold":
        print("you have folded")
        exit()
    elif user_input=="bet":
        
        bet1=input('how much would you like to bet?')
        while True:
            if bet1.isnumeric() :
                bet=int(bet1)
                money=money-bet
                pot=pot+bet+bet
                print("Bot1 calls")
                print(f"current pot:{pot}")
                break
                
            else:
                print("karl's a bum")
                time.sleep(0.1)
        break
    elif user_input=='check':
        print("Bot 1 checks")
        break
    else:
        print("I would like to politely request that you refrain from testing my program's capabilities.")


print()
print()
print("Current pot: ",pot)
print("turn:")
print(turn)
print()
print()

while 1==1:
    user_input=input("What action would you like to take?(check,bet,fold)")
    if user_input=="fold":
        print("you have folded")
        exit()
    elif user_input=="bet":
        
        bet1=input('how much would you like to bet?')
        
        while True:
            if bet1.isnumeric() :
                bet=int(bet1)
                money=money-bet
                pot=pot+bet+bet
                print("Bot1 calls")
                print(f"current pot:{pot}")
                break
                
            else:
                print("julian's a bum")
                time.sleep(0.1)
        break

    elif user_input=='check':
        print("Bot 1 checks")
        break
    else:
        print("STOP TESTING MY CODE I PUT IN FAIL-SAFES!!!")


print()
print()
print("Current pot: ",pot)
print("river:")
print(river)
print()
print()
while 1==1:
    user_input=input("What action would you like to take?(check,bet,fold)")
    if user_input=="fold":
        print("you have folded")
        exit()
    elif user_input=="bet":
        
        bet1=input('how much would you like to bet?')
        
        while True:
            if bet1.isnumeric() :
                bet=int(bet1)
                money=money-bet
                pot=pot+bet+bet
                print("Bot1 calls")
                print(f"current pot:{pot}")
                break
                
            else:
                print("chicken")
                time.sleep(0.1)
        break

    elif user_input=='check':
        print("Bot 1 checks")
        break
    else:
         while 1==1:
             print()
             time.sleep(0.1)
             print("STOP MESSING WITH MY CODE!!!!")
             time.sleep(0.1)


print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print("Your hand:")
print(hand1)
print(hand2)
print()
print()
print("Enemy's hand:")
print(bot1)
print(bot2)
print()
print()
print("Community Cards:")
print(flop1)
print(flop2)
print(flop3)
print(turn)
print(river)
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
score=0
bot_score=0
score=hand1v+hand2v
bot_score=bot1v+bot2v
if hand1v==flop1v or hand1v==flop2v or hand1v==flop3v or hand1v==turnv or hand1v==riverv or hand1v==hand2v:
    score=score+100
if hand2v==flop1v or hand2v==flop2v or hand2v==flop3v or hand2v==turnv or hand2v==riverv or hand2v==hand1v:
    score=score+100
if bot1v==flop1v or bot1v==flop2v or bot1v==flop3v or bot1v==turnv or bot1v==riverv or bot1v==bot2v:
    bot_score=bot_score+100
if bot2v==flop1v or bot2v==flop2v or bot2v==flop3v or bot2v==turnv or bot2v==riverv or bot2v==bot1v:
    bot_score=bot_score+100











def evaluate_hand(values):
    counts = Counter(values)
    count_values = list(counts.values())
    unique_values = sorted(set(values), reverse=True)

    if 4 in count_values:
        return (7, counts.most_common(1)[0][0]) 
 
    
    
    elif 3 in count_values:
        return (3, counts.most_common(1)[0][0]) 
    
    elif count_values.count(2) == 2:
        pairs = [val for val, count in counts.items() if count == 2]
        return (2, max(pairs))  
    
    elif 2 in count_values:
        return (1, counts.most_common(1)[0][0])  
    
    else:
        return (0, max(unique_values)) 


player_values = [hand1v, hand2v, flop1v, flop2v, flop3v, turnv, riverv]
bot_values = [bot1v, bot2v, flop1v, flop2v, flop3v, turnv, riverv]


player_rank, player_high = evaluate_hand(player_values)
bot_rank, bot_high = evaluate_hand(bot_values)

rank_names = ["High Card", "One Pair", "Two Pair", "Three of a Kind", "", "", "Full House", "Four of a Kind"]

print()
print("Final Hand Strengths:")
print(f"Your best hand: {rank_names[player_rank]} (High: {player_high})")
print(f"Bot's best hand: {rank_names[bot_rank]} (High: {bot_high})")
