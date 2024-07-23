# Let's play snake water game!!!
'''
s = snake
w = water
g = gun
'''
while True:
    import random

    computer = random.choice([0,1,-1])
    youstr = input("Enter your choice: ")
    youdict = {"s":0,"w":1,"g":-1}
    reversedict = {0:"snake",1:"water",-1:"gun"}

    you = youdict[youstr]

    # NOw we have two variables, You and Computer

    print(f"You chose {reversedict[you]} and computer chose {reversedict[computer]}")

    if(computer == you):
        print("It\'s draw")

    else:
        if(computer == 0 and you == 1):
            print("YOU LOSE!!")
        elif(computer == 0 and you == -1):
            print("YOU WON!!")
        elif(computer == 1 and you == 0):
            print("YOU WON!!")
        elif(computer == 1 and you == -1):
            print("YOU LOSE!!")
        elif(computer == -1 and you == 0):
            print("YOU LOSE!!")
        elif(computer == -1 and you == 1):
            print("YOU WON!!")
        else:
              print("INVALID INPUT!!")