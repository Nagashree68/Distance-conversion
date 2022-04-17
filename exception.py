income = 0
try:
    income = int(input("enter the income"))

except ValueError:
    print("wrong input entered,please correct it! and enter integer only")


print(income)