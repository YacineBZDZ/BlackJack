import random;
#from replit import clear
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
i = 11

Launch_Game = input("Do you want to play a game of Blackjack? Type 'Y' or 'N':")

def calculate_score(dict1, dict2): 
  score1 = sum(dict1)
  score2 = sum(dict2)
  return score1, score2

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
  dict_cards['card1'].extend([random.choice(cards),random.choice(cards)])
  dict_cards['card2'].extend([random.choice(cards),random.choice(cards)])
  user_cards =  dict_cards['card1']
  dealer_cards = dict_cards['card2']
  print(art.logo)
  user_score, dealer_score = calculate_score(user_cards,dealer_cards)
  print(f"Your cards are: {user_cards} , current score : {user_score} \n dealer first card is: {dealer_cards[0]} ")

  CheckAce(user_cards, user_score, dealer_cards, dealer_score)
  
  while(user_score <= 21 and player_take_card == True):
   Choose = input(f"Type 'Y' to get another card, type 'N' to pass: ")
   if(Choose == "Y" and user_score <= 21 ):
     user_cards.append(random.choice(cards))
     user_score, dealer_score = calculate_score(user_cards,dealer_cards)
     print(f"Your cards are: {user_cards} , current score : {user_score} \n dealer first card is: {dealer_cards[0]}")

   elif(Choose == "N"):
      break
  while(dealer_score <= 21):
    NewCard = random.choice(cards)
    takeOrNo = NewCard + dealer_score
    if(takeOrNo < 21):
      #print(f"Dealer gets a {NewCard}")
      dealer_cards.append(NewCard)
      user_score, dealer_score = calculate_score(user_cards,dealer_cards)
    else:
      break
      
  
  CheckAce(user_cards, user_score, dealer_cards, dealer_score)
  user_score, dealer_score = calculate_score(user_cards,dealer_cards)

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