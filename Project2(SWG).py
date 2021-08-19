import random
lst=["S","W","G"]

attempts=0
user_point=0
comp_point=0
chance=10
while attempts < chance:
    print("WELCOME TO SNAKE WATER GUN GAME!")
    user=input("enter your choice(Snake(S),Water(W),Gun(G)):")
    comp=random.choice(lst)

    if user=="S" and comp=="S":
        print("Tie")
        print("\nYou and computer both choose snake!")
        print("No one get the point\n")

    elif user=="W" and comp=="W":
        print("Tie")
        print("\nYou and computer both choose water!")
        print("No one get the point\n")

    elif  user=="G" and comp=="G":
        print("Tie")
        print("\nYou and computer both choose gun!")
        print("No one get the point\n")

    elif  user=="G" and comp=="W":
        comp_point=comp_point+1
        print("\nYou chose gun and computer choose water")
        print("Computer Won this round!\n")
        print("Computer get 1 point\n")

    elif  user=="G" and comp=="S":
        user_point=user_point+1
        print("\nYou chose gun and computer choose snake")
        print("You Won this round!\n")
        print("You get 1 point\n")

    elif  user=="S" and comp=="W":
        user_point=user_point+1
        print("\nYou chose snake and computer choose water")
        print("You Won this round!\n")
        print("You get 1 point\n")

    elif  user=="S" and comp=="G":
        comp_point=comp_point+1
        print("\nYou chose snake and computer choose gun")
        print("Computer Won this round!\n")
        print("Computer get 1 point\n")

    elif  user=="W" and comp=="S":
        comp_point=comp_point+1
        print("\nYou chose water and computer choose snake")
        print("Computer Won this round!\n")
        print("Computer get 1 point\n")

    elif  user=="W" and comp=="G":
        user_point=user_point+1
        print("\nYou chose water and computer choose gun")
        print("You Won this round!\n")
        print("You get 1 point\n")

    else:
        print("Invalid input!\n")
    
    attempts = attempts+1
    print(f"{chance-attempts} is left out of 10\n")

print("Game Over")

if comp_point==user_point:
    print("Tie!\n")
elif comp_point>user_point:
    print("Computer wins and you loose\n")
else:
    print("You wins and computer loose\n")
print(f"Your point is {user_point} and Computers point is {comp_point}")
    