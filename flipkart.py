mobile_price =15999
is_google_pay = True
if is_google_pay:
    discount = 0.2*mobile_price
else:
    discount = 0.1*mobile_price

print("Discounted amount", discount)
print(f"discounted price: {discount}")