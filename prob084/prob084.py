import prob084func
import random

#This program produced the correct answer even though I didn't implement
# the three doubles, go to jail rule.

trials = 0
diemax = 4
position = 0

posCount = {}
i = 0
while i < 40:
    posCount[i] = 0
    i += 1

chCards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
ccCards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#shuffle ch and cc cards
random.shuffle(chCards)
random.shuffle(ccCards)

#ch and cc card positions (top of deck)
chCardPos = 0
ccCardPos = 0

#print('Chance:', chCards)
#print('C Chest:', ccCards)

while trials <= 100000:

    die1 = random.randint(1, diemax)
    die2 = random.randint(1, diemax)
    total = die1 + die2

    position = (position + total) % 40 # Raw position

    #Position modifiers
    #Go 2 Jail
    if position == 30:
        position = 10
    #Community Chest
    elif position == 2 or position == 17 or position == 33:
        position = prob084func.cchestCards(chCards, chCardPos, position)
        chCardPos = (chCardPos + 1) % 16

    #Chance
    elif position == 7 or position == 22 or position == 36:
        position = prob084func.chanceCards(ccCards, ccCardPos, position)
        ccCardPos = (ccCardPos + 1) % 16

    posCount[position] += 1

    #print(die1, die2, ' = ', total, '\t', position, '\t', problem84func.pos2name(position))


    trials += 1

for space in posCount:
    print(space, ', ', prob84func.pos2name(space), ', ', posCount[space])
