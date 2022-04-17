Secret_number = 9
guess_count = 0
while guess_count < 3:
    guess= int(input("guess:"))
    guess_count=guess_count+1
    if guess == Secret_number:
        print("you won!")
        break
else:
    print("wrong guess sorry!")