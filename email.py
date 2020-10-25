"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""


addresses = []

#asks user if they have an email address to enter, user must input yes or no
more = input("Do you have an email address to enter (y/n)? ")

#gets user input on email

#asks users to for email address to enter
while more == "y":
#this is a loop which gets user input
    email = input("Enter the address: ")
    addresses.append(email)
#if yes then enter email
#Asks user to input another address
    more = input("Do you have another address(y/n)? ")
    while more != "y":
        if more == "n":
            break
        else:
            more = input("Please enter a y or n: ")
#these lines of code is a loop that will either get another email address if yes or print only the one email entered
#prints email addresses    
print(addresses)

