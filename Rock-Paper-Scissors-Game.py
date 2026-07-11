import random
l1=["ROCK","PAPER","SCISSORS"]
d1={1:"ROCK",2:"PAPER",3:"SCISSORS"}
pl_score=0
com_score=0
def player_input():
    return int(input("Enter your choice\n1.ROCK\n2.PAPER\n3.SCISSORS"))
def computer_input():
    return random.choice(l1)
def winner(pl_choice,com_choice):
    global pl_score,com_score
    print("Your choice-",d1[pl_choice])
    print("Computer choice-",com_choice)
    if pl_choice == 1:
        if com_choice == "ROCK":
            print("GAME TIE\n!!")
        elif com_choice == "PAPER":
            print("COMPUTER WINS!!\n")
            com_score += 1
        else:
            print("YOU WIN!!\n")
            pl_score += 1
    if pl_choice == 2:
        if com_choice == "ROCK":
            print("YOU WIN\n!!")
            pl_score += 1
        elif com_choice == "PAPER":
            print("GAME TIE!!\n")
        else:
            print("COMPUTER WINS!!\n")
            com_score += 1
    if pl_choice == 3:
        if com_choice == "ROCK":
            print("COMPUTER WINS\n")
        elif com_choice == "PAPER":
            print("YOU WIN!!")
        else:
            print("GAME TIE!!\n")
            
def final_result():
    print("PLAYER's SCORE",pl_score)
    print("COMPUTER's SCORE",com_score)
    if pl_score > com_score:
        print("*****PLAYER WON THE GAME*****")
    elif pl_score < com_score:
        print("*****COMPUTER WON THE GAME*****")
    else:
        print("*****GAME DRAW*****")

print("***WELCOME TO ROCK-PAPER-SCISSORS GAME***\n")
n=int(input("<<-Enter number of games you want to play->>"))
round_no=1
while n>0:
      print(f"***ROUND{round_no}***")
      pl_choice = player_input()
      if pl_choice not in [1,2,3]:
          print("YOU ENTERED WRONG")
          continue
      com_choice = computer_input()
      winner(pl_choice,com_choice)
      n-=1
      round_no += 1
final_result()
            