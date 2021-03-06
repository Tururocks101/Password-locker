from user import Credentials
from user import User

# new_account is an instance of Credentials class. Contains details for one account
# new_user is an instance of User class. Contains username and password of lock room user


def create_user(lock_owner, lock_key):
    '''
    function to create a new user
    '''
    new_user = User(lock_owner, lock_key)
    return new_user


def save_user(data):
    '''
    function to save a new user
    '''
    data.save_user()


def create_account(account, u_name, passwd):
    '''
    function to create a new account
    '''
    new_account = Credentials(account, u_name, passwd)
    return new_account


def save_accounts(credentials):
    '''
    function to save the new account
    '''
    credentials.save_account()


def delete_accounts(credentials):
    '''
    function to delete an account
    '''
    credentials.delete_account()


def search_accounts(search):
    '''
    function to find an account by account name
    '''
    return Credentials.search_accounts(search)


def generate_password():
    '''
    function to generate a password
    '''
    random_password = Credentials.password_generate()
    return random_password


def display_account():
    '''
    function to display all accounts saved
    '''
    return Credentials.display_accounts()


def main():

    print("\nWelcome!")
    print("\n 1. Create an account \n 2. Exit app")
    option = input()

    if option == '1':
        print("Enter your username")
        lock_owner = input()
        if not lock_owner:
            print("You must type something in")
        else:
            print("Enter a password")
            lock_key = input()
            if not lock_key:
                print("You must type something in")
            else:
                save_user(create_user(lock_owner, lock_key))
                print("-"*10)
                print(f"{lock_owner}, please enter your password again to login.")
                confirm = input()
                if confirm == lock_key:
                    print("\n You are successfully logged in!")
                    while True:
                        print("-"*10)
                        print("What will you be doing today? \n Use these short codes : \n \t\t aa - Add an account using your own password \n \t\t ca - Generate a password for your new account \n \t\t ba - display saved accounts \n \t\t fa - Search for an account \n \t\t D - delete an account \n \t\t ex - Exit the locker room ")
                        short_code = input().lower()

                        if short_code == 'aa':
                            print("-"*10)
                            print("Enter an existing account")
                            print("Account name ....(eg: twitter)")
                            account = input()
                            print("Username ...")
                            u_name = input()
                            print("Password ...")
                            passwd = input()
                            save_accounts(create_account(account, u_name, passwd))
                            print('\n')
                            print(
                                f"New account: {account} added \n Username: {u_name} --- Password:{passwd}")
                            print('\n')

                        elif short_code == 'ca':
                            print("-"*10)
                            print("Account name ....(eg: twitter)")
                            account = input()
                            print("Username ...")
                            u_name = input()
                            print("...........")
                            passwd = generate_password()
                            save_accounts(create_account(account, u_name, passwd))
                            print('Your account has been created successfully!\n')
                            print(
                                f"New account: {account} \n Username: {u_name} --- Password:{passwd}")
                            print('\n')

                        elif short_code == 'ba':
                            print("-"*10)
                            if display_account() != []:
                                print("\nHere is a list of all your accounts:\n")
                                for item in display_account():
                                    print(item.account_name + "\t --> " +
                                          item.username + "\t --> " + item.password)
                            else:
                                print("\n You do not have any accounts saved \n")

                        elif short_code == 'fa':
                            print("-"*10)
                            print("\n Enter an account type to search. eg:Twitter\n")
                            search = input()
                            if search_accounts(search):
                                found = search_accounts(search)
                                print("\n Here's what we've found:\n")
                                print(found.account_name + "\t" +
                                      found.username + "\t" + found.password)

                        elif short_code == 'd':
                            print("-"*10)
                            print("Enter the account name for the record you want to delete eg: Twitter")
                            item = input()
                            if search_accounts(item):
                                delete_accounts(search_accounts(item))
                                print("-"*10)
                                print("The account has been deleted successfully")
                                print("Here is a list of your remaining accounts:\n")
                                for remaining in display_account():
                                    print(remaining.account_name + "\t --> " +
                                          remaining.username + "\t --> " + remaining.password)
                            else:
                                print("There is no record of the item you are trying to delete")

                        elif short_code == "ex":
                            print("-"*10)
                            print(f"Have a wonderful day, {lock_owner}")
                            break
                        else:
                            print("-"*10)
                            print("\nInvalid short code. Please try again\n")
                else:
                    print("-"*10)
                    print("\nIncorrect password. Try again")
    elif option == '2':
        print("-"*10)
        print(f"\nHave a wonderful day, {lock_owner}")
    else:
        print("-"*10)
        print("\nInvalid option. Enter valid code to continue")


if __name__ == "__main__":
    main()
