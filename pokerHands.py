def sameSuit(suits): 
	return suits.count(suits[0])==5

def isCons(newcardno):
	return (sorted(newcardno) == list(range(min(newcardno), max(newcardno)+1)))

def changeToInts(cardno):
	newcardno = []

	for i in range(0, len(cardno)):
		if (cardno[i] == 'A'):
			newcardno.append(14)
		elif (cardno[i] == 'K'):
			newcardno.append(13)
		elif (cardno[i] == 'Q'):
			newcardno.append(12)
		elif (cardno[i] == 'J'):
			newcardno.append(11)
		elif (cardno[i] == 'T'):
			newcardno.append(10)
		else:
			newcardno.append(int(cardno[i]))
	return newcardno


def getValue(hand):
	suits = []
	cardno = []
	for i in range(1, 14, 3):
		suits.append(hand[i])
	for i in range(0, 14, 3):
		cardno.append(hand[i])



	if ((sorted(cardno) == ['A', 'J', 'K', 'Q', 'T'])) & sameSuit(suits):
		#royal flush
		return 10

	if (isCons(changeToInts(cardno)) & sameSuit(suits)):
		#straight flush
		return 9

	if (max(dict((x,cardno.count(x)) for x in set(cardno)).values()) == 4):
		#four of a kind
		return 8
	

	if ((max(dict((x,cardno.count(x)) for x in set(cardno)).values()) == 3) & (min(dict((x,cardno.count(x)) for x in set(cardno)).values())==2)):
		#full house
		return 7

	if sameSuit(suits):
		#flush
		return 6


	if (isCons(changeToInts(cardno))):
		#straight
		return 5

	if (max(dict((x,cardno.count(x)) for x in set(cardno)).values()) == 3):
		#three of a kind
		return 4
	
	if ((len(dict((x,cardno.count(x)) for x in set(cardno)).values())==2) & (max(dict((x,cardno.count(x)) for x in set(cardno)).values())==2) & min(dict((x,cardno.count(x)) for x in set(cardno)).values())==1):
		#two pair
		return 3

	if (max(dict((x,cardno.count(x)) for x in set(cardno)).values()) == 2):
		#three of a kind
		return 2

	else:

		return str(max(changeToInts(cardno)))




def main():

	player1 = 0
	player2 = 0
	draws = 0

	with open('poker_input.txt', 'r') as f:
		hands = f.read().splitlines()
	f.close()

	player1hand = []
	player2hand = []

	for hand in hands:
		player1hand.append(hand[0:14])
		player2hand.append(hand[15:29])



	for i in range(len(player1hand)):
		if((type(getValue(player1hand[i]))==str) & (type(getValue(player2hand[i]))!=str)):
			player2 +=1
		elif((type(getValue(player1hand[i]))!=str) & (type(getValue(player2hand[i]))==str)):
			player1 +=1
		elif((type(getValue(player1hand[i]))==str) & (type(getValue(player2hand[i]))==str)):
			if int(getValue(player1hand[i]))<int(getValue(player2hand[i])):
				player2+=1
			elif int(getValue(player1hand[i]))>int(getValue(player2hand[i])):
				player1+=1
			else:
				draws +=1
				continue

		else:
			if getValue(player1hand[i])>getValue(player2hand[i]):
				player1 += 1
			elif getValue(player1hand[i])<getValue(player2hand[i]):
				player2 += 1
			else:
				draws+=1
				continue
			
	if player1>player2:
		print("Congratulations, Player 1 is the winner!")
	else:
		print("Congratulations, Player 2 is the winner!")


if __name__=='__main__':
	main()
