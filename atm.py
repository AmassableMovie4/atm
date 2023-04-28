from cardHolder import cardHolder

def print_menu():
    print("Please select from an option below:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")
    
def deposit(cardHolder):
    try:
        deposit = float(input("How much would you like to deposit? "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print(f"Thank you for your deposit. Your new balance is ${cardHolder.get_balance()}")
    except:
        print("Invalid input. Please try again.")
    
    def withdraw(cardHolder):
        try:
            withdraw = float(input("How much would you like to withdraw? "))
            ### Check if user has enough funds
            if(cardHolder.get_balance() > withdraw):
                print("Insufficient funds. Please try again.")
            else:
                cardHolder.set_balance(cardHolder.get_balance() - withdraw)
                print(f"Thank you for your withdrawal. Your new balance is ${cardHolder.get_balance()}")
        except:
            print("Invalid input. Please try again.")
            
    
    def check_balance(cardHolder):
        print(f"Your current balance is ${cardHolder.get_balance()}")
        
    if __name__ == "__main__":
        current_user = cardHolder("","","","","")
        
        ### Create a repo of cardholders
        list_of_cardHolders = []
        list_of_cardHolders.append(cardHolder())
        
        debitCardNum = ""
        while True:
            try:
                debitCardNum = input("Please enter your card number: ")
                ### check against repo
                debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
                if(len(debitMatch) > 0):
                    current_user = debitMatch[0]
                    break
                else:
                    print("Invalid card number. Please try again.")
            except:
                print("Invalid card number. Please try again.")
        
        
while True:
    try:
        userPin = int(input("Please enter your PIN: ").strip())
    except:
        print("Invalid PIN. Please try again.")
    
    print("Welcome", current_user.get_firstname(), " :)")
    option = 0
    while (True):
        print_menu()
        try:
            option = int(input("Please select an option: "))
        except:
            print("Invalid option. Please try again.")
            
        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        elif(option == 4):
            break
        else:
            option = 0
        
        print("Thank you for using our bank. Goodbye!")