import random #Importing the random module

def choose():
    words=['Scientist','Robot','Python','School','College','Cricket''Foot ball','Volleyball','India','Pakistan','China','Afganistan','Uzbekistan','Punjab','Delhi','Maharashtra']
    pick=random.choice(words)
    return pick


def jumble(word):
    random_word=random.sample(word,Len(word))
    jumbled=''.join(random_word)
    return jumbled
 
def thank(p1name,pl2name,p1,p2):
    print(p1name,'Your score is:',p1)
    print(p2name,"Your score is:",p2)
    check_win(p1name,p2name,p1,p2)
    print("Thanks for playing.......")


def check_win(player1,player2,p1score,p2score):
    if  p1score>p2score:
        print("Winner is :",player1)
    elif p2score>p1score:
        print("Winner is :",player2)
    else:
        print("Draw... !!!Well played guys!!!")

def play():
    p1name=input("Enter the name of the player 1:")
    p2name=input("Enter the name of the player 2:")
    pp1=0
    pp2=0
    turn=0

    while True:
        picked_word=choose()
        question=jumble(picked_word)
        print("The jumbled word is:",question)
        if turn%2==0:
            print(p1name,'Your turn')
            ans=input("Whats in your mind?")
            if ans==picked_word:
                pp1 += 1
                print("Your score is :".pp1)
                turn += 1
            else:
                print("Better luck next time.....")
                
                print(p2name,'Your turn')
                ans=input("What is in your mind?")
                if ans==picked_word:
                    pp2 += 1
                    print("Yor score is :",pp2)
                else:
                    print("Better luck next time.... correct word is :",picked_word)
                c=int(input("Press 1 to continue and 0 to quit :"))
                if c==0:
                    thank(p1name,p2name,pp1,pp1)
                    break
                else:
                     print(p2name,'Your turn')
                     ans=input("What is in your mind?")
                    if ans==picked_word:
                              pp2 += 1
                            print("Yor score is :",pp2)
                    else:
                        print("Better luck next time.... correct word is :",picked_word)
                    

          





