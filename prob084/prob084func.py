def pos2name(position):
	spacenames = {0: 'GO', 1: 'A1', 2: 'CC1', 3: 'A2', 4: 'T1',
		      5: 'R1', 6: 'B1', 7: 'CH1', 8: 'B2', 9: 'B3', 10: 'JAIL',
		      11: 'C1', 12: 'U1', 13: 'C2', 14: 'C3', 15: 'R2', 
		      16: 'D1', 17: 'CC2', 18: 'D2', 19: 'D3', 20: 'FP',
		      21: 'E1', 22: 'CH2', 23: 'E2', 24: 'E3', 25: 'R3',
		      26: 'F1', 27: 'F2', 28: 'U2', 29: 'F3', 30: 'G2J',
		      31: 'G1', 32: 'G2', 33: 'CC3', 34: 'G3', 35: 'R4',
		      36: 'CH3', 37: 'H1', 38: 'T2', 39: 'H2'}
	position = int(position)
	return spacenames[position]

def chanceCards(chCards, chCardPos, position):

	card = chCards[chCardPos]

	if card == 1:
		#Advance to GO
		newpos = 0
	elif card == 2:
		#Go to JAIL
		newpos = 10
	elif card == 3:
		#Go to C1
		newpos = 11
	elif card == 4:
		#Go to E3
		newpos = 24
	elif card == 5:
		#Go to H2
		newpos = 39
	elif card == 6:
		#Go to R1
		newpos = 5
	elif card == 7 or card == 8:
		#Go to next railroad
		newpos = nextRR(position)
	elif card == 9:
		#Go to next Utilitiy
		newpos = nextUtil(position)
	elif card == 10:
		#Go back 3 spaces
		newpos = position - 3
	else:
		newpos = position

	#print('Chance: card ', card, ' pos ' , position, ' new ', newpos)

	return newpos

def cchestCards(ccCards, ccCardPos, position):

	card = ccCards[ccCardPos]

	if card == 1:
		#Advance to GO
		position = 0
	elif card == 2:
		#Go to JAIL
		position = 10

	return position

def nextRR(position):
	if position < 5 or position > 35:
		return 5
	elif 5 < position < 15:
		return 15
	elif 15 < position < 25:
		return 25
	elif 25 < position < 35:
		return 25
	else:
		exit('Error nextRR')

def nextUtil(position):
	if position < 12 or position > 28:
		return 12
	elif 12 < position < 28:
		return 28
	else:
		exit('Error nextUtil')
