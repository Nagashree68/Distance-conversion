def welcome_amazon_greet():
    print("Hello Rakesh")
    print("Welcome to Amazon family")

welcome_amazon_greet()

def welcome_amazon_greet(is_buyer):

    if(is_buyer):
        print("Hello Rakesh")
        print("Welcome to Amazon buyer family")
    else:
        print("hello Rakesh")
        print("welcome to amazon vendor family")

welcome_amazon_greet(False)

def welcome_amazon_greet(is_buyer,name):
    print("Hello"+name)

    if(is_buyer):

        print("Welcome to Amazon buyer family")
    else:

        print("welcome to amazon vendor family")

welcome_amazon_greet(False,"Nag")