for character in "microdegree":
    print(character)

name_list = ["nag", "darshi","priyu"]
for indi in name_list:
    print(indi)

Name_list = ["nag", "darshi","priyu"]
for indi in range(1,2):
    print(indi)
    print(Name_list[indi])

Name_list = ["nag", "darshi","priyu"]
for indi in range(len(Name_list)):
    if(Name_list[indi] == "nag"):
        print(f"found nag {indi}")
