'''
Author;Alan Binu
Date:28-10-2024
Description:'a program that simulates a simple bank ATM system.
 The user has an initial balance of $1000.
 The ATM should display a menu with options to':
'''
balance_amount=1000
while True:
    print('1.\tCheck Balamce')
    print('2.\tDeposit Money')
    print('3.\tWithdraw Money')
    print('4.\tExit')
    choice=int(input('enter your choice'))
    if choice==1:
        print(f"the current balance ${balance_amount}")
    elif choice==2:
        deposit_amount=float(input('enter the amount'))
        balance_amount=balance_amount+deposit_amount
        print(f'the deposited amount ${deposit_amount} and  '
              f'the current balance ${balance_amount}')
    elif choice==3:
        withdraw_amount=float(input("enter the amount to withdraw"))
        balance_amount=balance_amount-withdraw_amount
        print(f"the amount withdrawn from the account"
              f"${withdraw_amount} the balance amount"
              f"${balance_amount}")
    elif choice==4:
        break
    else:
        print('invalid entry')
