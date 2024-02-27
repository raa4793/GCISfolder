'''
Group 5 members: Lana Kendakji (lk3501), Raza Ali (raa4793), Noor Aldin Mohsi (nm6914)
Brief description: We have used the skills we learnt in class such as defining functions,
if and else satements and while true loops to create this program.
github repsoitory:
lana = https://github.com/lk3501/GCIS123.git
Raza = https://github.com/raa4793/GCISfolder
Noor Aldin = https://github.com/NourAldin278/rit 
'''

#first begin by defining rates of conversion (information found on the web)
AED_TO_EURO_RATE=0.25
AED_TO_GBP_RATE=0.21
AED_TO_USD_RATE=0.27

#begin by defining conversion functions
def aed_to_eur(money): #money is parameter and we will ask user for input
    convertedvalue = money*AED_TO_EURO_RATE
    return convertedvalue

def aed_to_britishPound(money):
    convertedvalue = money*AED_TO_GBP_RATE
    return convertedvalue

def aed_to_dollar(money):
    convertedvalue = money*AED_TO_USD_RATE
    return convertedvalue

def eur_to_aed(amount): #amount is parameter and we will ask user for input
    convertedvalue = amount/AED_TO_EURO_RATE
    return convertedvalue

def britishPound_to_aed(amount):
    convertedvalue = amount/AED_TO_GBP_RATE
    return convertedvalue

def dollar_to_aed(amount):
    convertedvalue = amount/AED_TO_USD_RATE
    return convertedvalue

def main(): #begin be defining main function
    while True: #while True loop in order to be able to return to main page
        print(" \"Main Menu\"") #use backwards slash in order to print the quotation marks as well
        print("Welcome to Currency Converter")
        print("---------------------------------")
        print("1. AED to other currencies")
        print("2. Other currencies to AED")
        print("3. Exit")
        user_input = int(input("Select the conversion direction(1/2/3): ")) #use int casting in order to only input a number

        if user_input == 1: #first option
            money = float(input("Enter your amount you want to convert:")) #enter amount of money as float as it can be in decimal
            print("1. AED to Euro (EUR)")
            print("2. AED to British Pound (GBP)")
            print("3. AED to US Dollar")
            print("4. AED to Exit")
            subchoice = int(input("Enter the Sub choice of currency(1/2/3/4): ")) #enter second direction
            if subchoice == 1:
                call = aed_to_eur(money)
                print(money,"AED is equal to", call, "EURO")
            elif subchoice == 2:
                call = aed_to_britishPound(money)
                print(money,"AED is equal to", call, "GBP")
            elif subchoice == 3:
                call = aed_to_dollar(money)
                print(money,"AED is equal to", call, "USD")
            elif subchoice == 4:
                print("Program is exit")
                break #use break to exit loop
            else: #else means any option other than numbers 1-4, we will show an error on this case
                print("Please enter a Valid option (1/2/3/4).")
                continue #in order to return to main page after error is made

        elif user_input == 2: #second option
            amount = float(input("Enter your amount you want to convert:")) #enter amount of money as float as it can be in decimal
            print("1. Euro (EUR) to AED")
            print("2. British Pound (GBP) to AED")
            print("3. Dollar to AED")
            print("4. AED to exit")
            subchoice = int(input("Enter the Sub choice of currency(1/2/3/4): ")) #enter second direction
            if subchoice == 1:
                call = eur_to_aed(amount)
                print(amount,"EUR is equal to", call,"AED")
            elif subchoice == 2:
                call = britishPound_to_aed(amount)
                print(amount,"GBP is equal to", call,"AED")
            elif subchoice == 3:
                call = dollar_to_aed(amount)
                print(amount,"USD is equal to", call,"AED")
            elif subchoice == 4:
                print("Program is exit")
                break #use break to exit loop
            else: #else means any option other than numbers 1-4, we will show an error on this case
                print("Please enter a Valid option (1/2/3/4).")
                continue #in order to return to main page after error is made

        elif user_input == 3: #third option
            print("Program is exit")
            break #exit loop

        else:
            print("Please Enter a Valid Option (1/2/3)")
            continue #in order to return to main page after erroe is made

        # Ask user if they want to continue
        continue_response = input("Do you want to continue (y/n): ")
        if continue_response == 'y':
            continue #bring back to main page
        elif continue_response == 'n':
            print("Program is exit")
            break #exit loop
        else: #else means any option other than y or n
                print("Please enter a Valid option (y/n).")
                continue #in order to return to main page after error is made


if __name__ == "__main__": 
    main() #call main

