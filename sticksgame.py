number_of_sticks=16
player1=input("Enter player 1 name:")
player2=input("Enter player 2 name:")
while number_of_sticks>0:
    if number_of_sticks>0:
        take=int(input("Enter the number of sticks you want to take upto 3"))
        number_of_sticks=(number_of_sticks-take)
        print(player1,"sticks remaining:",number_of_sticks)
    elif number_of_sticks<=0:
        print(player1,"is the loser")
        break
    if number_of_sticks>0:
        take=int(input("Enter the number of sticks "))
        number_of_sticks= number_of_sticks-take
        print(player2,"sticks remaining:",number_of_sticks)

    elif number_of_sticks<=0:
        print(player2,"is the loser")
        break