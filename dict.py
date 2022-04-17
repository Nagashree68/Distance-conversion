
#aadhar form
form_name = {
    "application name" : "nag",
    "mobile number" : 99987689,
    "email_id" : "grnag@gmail.com",
    "is_acepted_t_c" : True
}

print(form_name["email_id"])
print(form_name)
print(form_name.get("photo"))
print(form_name.get("email_id","key value doesn't exist"))
print(form_name.get("photo","key value doesn't exist"))
form_name["age"] = 54
print(form_name)
form_name["email_id"]="gagan@gmail.com"
print(form_name)