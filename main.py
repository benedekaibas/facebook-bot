#C:\Users\kaiba\OneDrive\Asztali gép\learning-python\fb_bot.py


#TODO: make the import workable, because it has missing elements problems
#import is working, but after running the code is still says modulenotfound error. solve this!
from fbchat import Client
from fbchat.models import Message
from fbchat.models import *

#this is just an example of an email and password
#sigzer187@gmail.com
#sodigeci9

def main():
    username = str(input("Enter your email address: \n"))
    password = input("Enter your password: \n")
    client = Client(username, password)

    #login 
    if not client.isLoggedIn():
        client.login()
    else:
        print("Error")
    




if __name__ == "__main__":
    main()

