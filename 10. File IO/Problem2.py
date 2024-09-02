#update a file
import random
def game():
    s=random.randint(1,100)
    print("The score is", s)
    with open("hi-score.txt") as f:
        hs=f.read()
        if(hs==""):
            hs=0
    if(int(s)>int(hs)):
        with open("hi-score.txt","w") as f:
            f.write(str(s))
        
game()