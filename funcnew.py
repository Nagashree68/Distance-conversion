def welcome_email(name):
    print("hello"+name)
    print("welcome!")
welcome_email("nag")

def welcome_email(first_name,last_name):
    print("hello"+first_name+" "+last_name)
    print("welcome!")
welcome_email("nag","shree")
welcome_email("shree","nag")
welcome_email(first_name="nag",last_name="shree")