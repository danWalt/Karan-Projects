from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount
from BusinessAccount import BusinessAccount

if __name__ == "__main__":
    checking = CheckingAccount()
    savings = SavingsAccount()
    business = BusinessAccount()
    rnd = 0
    while rnd < 10:
        checking.deposit(1000)
        savings.deposit(2000)
        business.deposit(50000)
        business.withdraw(30000)
        savings.apply_interest()
        business.apply_interest()
        print('Do you want to see any of the accounts details? 1- yes 2- no')
        user_choice = input()
        if user_choice == '1':
            print(
                'Do you want to see any of the accounts details? please '
                'select a number between 1 and 3.')
        else:
            break
        if user_choice == '1':
            print('Which account are you interested in? 1- checking 2- '
                  'savings 3- business')
            account = int(input())
            if account == 1:
                account = checking
            elif account == 2:
                account = savings
            else:
                account = business
            print('What do you want to see?'
                  '1- balance'
                  '2- deposit limit'
                  '3- withdraw limit'
                  '4- interest rate')
            option_to_see = int(input())
            if option_to_see == 1:
                print(account.get_balance())
            elif option_to_see == 2:
                print(account.get_deposit_limit())
            elif option_to_see == 3:
                print(account.get_withdraw_limit())
            else:
                print(account.get_interest_rate())
        else:
            print('Thank you and have a nice day')
        rnd += 1