import random
computer=random.choice([-1,1,0])
s={"snake":1, "water": 0, "gun":-1}
w={1:"snake", 0:"water", -1:"gun"}
g=input("snake, water, gun, choose any one")
choice=s[g]

if (choice==1 and computer==1) or (choice==-1 and computer==-1) or(choice==0 and computer==0):
    print(f"Computer chose {w[computer]}\nYou chose {g}\nGame is draw!")

elif (choice==1 and computer==-1) or (choice==0 and computer==1) or (choice==-1 and computer==0):
    print(f"Computer chose {w[computer]}\nYou chose {g}\nYou lost the game :(")

elif (choice==-1 and computer==1) or (choice==1 and computer==0) or (choice==0 and computer==-1):
    print(f"Computer chose {w[computer]}\nYou chose {g}\nYou win!")

