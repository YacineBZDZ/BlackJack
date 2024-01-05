import random;
#from replit import clear
import art
def takeCard():
 cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 card = random.choice(cards)
 return card
i = 11

Launch_Game = input("Do you want to play a game of Blackjack? Type 'Y' or 'N':")
#change this code because of redundancy
def calculate_score(cards): 
  score = sum(cards)
  return score

def CheckAce(userCards, userScore, dealerCards, dealerScore):
  lose = userScore + 11
  dealerLose = dealerScore + 11
  if i in userCards and userScore > 10 and userScore != 21 and lose > 21:
    ace = user_cards.index(11)
    #print(f"the index of the ace :{ace} \n the card value of the ace is : {user_cards[ace]}")
    user_cards[ace] = 1
  elif i in dealerCards and dealerScore < 10 and dealerScore != 21 and dealerLose > 21:
    aceDealer = dealer_cards.index(11)
    #print(f"the index of the ace :{ace} \n the card value of the ace is : {user_cards[ace]}")
    dealer_cards[aceDealer] = 1
  
while(Launch_Game == "Y"):
  dict_cards = {}
  player_take_card = True
  dict_cards = {"card1": [], "card2": []}
  user_score = 0
  dealer_score = 0
  Choose =""
  #need to be changed withe angela's code 
  for _ in range(2):
    dict_cards['card1'].append(takeCard())
    dict_cards['card2'].append(takeCard())
  user_cards =  dict_cards['card1']
  dealer_cards = dict_cards['card2']
  print(art.logo)
  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards)

  print(f"Your cards are: {user_cards} , current score : {user_score} \n dealer first card is: {dealer_cards[0]} ")

  CheckAce(user_cards, user_score, dealer_cards, dealer_score)
  
  while(user_score <= 21 and player_take_card == True):
   Choose = input(f"Type 'Y' to get another card, type 'N' to pass: ")
   if(Choose == "Y" and user_score <= 21 ):
     user_cards.append(takeCard())
     user_score = calculate_score(user_cards)
     print(f"Your cards are: {user_cards} , current score : {user_score} \n dealer first card is: {dealer_cards[0]}")

   elif(Choose == "N"):
      break
  while(dealer_score <= 21):
    NewCard = takeCard()
    takeOrNo = NewCard + dealer_score
    if(takeOrNo < 21):
      #print(f"Dealer gets a {NewCard}")
      dealer_cards.append(NewCard)
      dealer_score = calculate_score(dealer_cards)
    else:
      break
      
  
  CheckAce(user_cards, user_score, dealer_cards, dealer_score)
  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards)


  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"dealer final hand: {dealer_cards}, final score: {dealer_score}")
  if(dealer_score == 21 and user_score == 21 or dealer_score == user_score):
    print("No one went over. It's a draw!")
  elif(dealer_score == 21):
    print("You Lose!")
  elif(user_score == 21):
    print("You win!")
  elif(user_score < 21 and dealer_score > 21):
    print("Opponent went over. You Win!")
  elif(dealer_score < 21 and user_score > 21):
    print("You went over. You Lose!")
  elif(dealer_score < 21 and user_score < dealer_score):
    print("Opponent Have a Biger Score. You Lose!")
  elif(user_score < 21 and dealer_score < user_score):
    print("You Have a Biger Score. You Win!")
  else:
    print("All went over. No one Wins!")
    
  
  
  Launch_Game = input("would you like to play Again?(Y/N)")
  #Clear()