Your_Score = 0
Computer_Score = 0
while 2<6:
    print("          ========================================== \n                   STONE - PAPER - SCISSOR \n          ==========================================")
    print()
    A = ("Select your choice (Stone, Paper, Scissor, Quit(To quit the game))")
    print(A)
    print()
    choice = input("Your choice : ")
    import random
    list2 = ["stone", "paper", "scissor"]
    value = random.choice(list2)
    print(f"Computer : {value}")
    print()
    if choice.lower() == value:
        print("Tie")
    elif choice.lower() == "stone" and value == "paper":
        print("Computer won")
        Computer_Score += 1
    elif choice.lower() == "paper" and value == "scissor":
        print("Computer won")
        Computer_Score += 1
    elif choice.lower() == "scissor" and value == "stone":
        print("Computer won")
        Computer_Score += 1
    elif choice.lower() == "paper" and value == "stone":
        print("You won")
        Your_Score += 1
    elif choice.lower() == "scissor" and value == "paper":
        print("You won")
        Your_Score += 1
    elif choice.lower() == "stone" and value == "scissor":
        print("You won")
        Your_Score += 1
    elif choice.lower() == "quit":
           Replay = input("Do you wish to quit(Yes/No) : ")
           if Replay.lower() == "yes":
                       break  
    else:
        print("Oops😪")
print()
print("                  x_________________________x")
print(f"          ==========================================  \n          |              SCORE BOARD               |\n          ========================================== \n          =    Your Score    =    Computer Score   = \n          =        {Your_Score}         =          {Computer_Score}          =")
print("          ==========================================")
print()
print("                  x_________________________x")
print()
print()
print()