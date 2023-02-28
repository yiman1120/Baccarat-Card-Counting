import os

cards = []
card_counting, DB_counting, count = 0, 0, 0
score = [0, 1, 1, 1, 2, -1, -2, -1, -1, 0]
DB_score = [-1.25, 1.83, 2.74, 3, 1.11, 0.41, 0.13, -1.33, -1.46, -1.43]
num_card = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while cards != 'N' or 'n':
  cards = input("Enter the card's number (0-9), if ended plz enter 'N': ")
  while cards == '':
    cards = input("Empty Entry. Enter the card's number (0-9): ")
  cards = int(float(cards[0]))

  count += 1
  num_card[cards] +=1
  
  card_counting += score[cards]
  # card_counting = card_counting / ((416 - count)/52)
  
  DB_counting += DB_score[cards]
  # DB_counting = DB_counting / ((416 - count)/52)

  # Clearing the Screen
  os.system('clear')

  print(f"count: {count}", end='\n\n')
  
  # print("True Count -> (Player/Banker):(16 or 16+/15 or 15-)")  
  print("Not very True Count -> (Player/Banker):(3+/(-3)-)")  
  if card_counting > 0:
    print(f"Card Counting Score: +{card_counting}", end='\n\n')
  else:
    print(f"Card Counting Score: {card_counting}", end='\n\n')

  # print("True Count -> (Player):(7 or 7+)") 
  print("Not very True Count -> (Player):(3+)") 
  if DB_counting > 0:
    print(f"* Dragon Bonus Score: +{DB_counting}", end='\n\n')
  else:
    print(f"* Dragon Bonus Score: {DB_counting}", end='\n\n')

  print('''The Effect of Removal (EOR)
    x | Remain | B | P | Tie
    ___________________________
    0 | {zero} | 188 | -178 | 5129
    1 | {one} | 440 | -448 | 1293
    2 | {two} | 552 | -543 | -2392
    3 | {three} | 649 | -672 | -2141
    4 | {four} | 1157 | -1195 | -2924
    5 | {five} | -827 | 841 | -2644
    6 | {six} | -1132 | 1128 | -11595
    7 | {seven} | -827 | 817 | -10914
    8 | {eight} | -502 | 533 | 6543
    9 | {nine} | -231 | 249 | 4260
    ___________________________\n\n'''
        .format(zero=128-num_card[0], one=32-num_card[1], two=32-num_card[2], three=32-num_card[3], four=32-num_card[4], five=32-num_card[5], six=32-num_card[6], seven=32-num_card[7], eight=32-num_card[8], nine=32-num_card[9]))