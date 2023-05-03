balance = 109 #Idealy should be taken from database
input('Hello! Welcome to M&T bank. If you are signing up press 1. If you are loggining in press 2.')
if input==1:
    print('You need to contact customer support or go visit your local M&T bank. This machine cannot vertify your photo id.')
if input==2:
    name=('What is your username?')
    password=('Hello {name}, its nice to see you again! What is your password?')
if {password}==True:
    print('----------------------------------------------------')
    choice=('What would you like to do today? Press 1 to check balance. Press 2 to modify your account. Press 3 to change your balance ')

if {choice}==1:
    print('Your balance is,${balance}')
    print('Thank you, goodbye.')

if {choice}==2:
    print('How would you like to modify your account? Press A to change your account password. Press B to change your email.')
    more=('Press C to change your balance. Press D to delete your account. All other modifications must be done in person.')

if {more}==A:
    changing==('What would you like your new account password to be?')
    print('Your M&T password is now {changing}.')

if {more}==B:
    email==('What would you like to change your email into?')
    print('Your email for this account is now {email}')
if {more}==C:
    money==('Do you want to withdraw(L) or deposit(G) money?')
if {money}==L:
    number('How much money are you routing number youre sending money to?')
    print('You have just send ${money} to the account holding the routing number of {number}')

if {more}==D:
    print('We are sorry that you felt that your time with M&T bank is coming to an end. We will welcome you back with open arms.')
    print('This account is deleted. ')
