Student_1 = {
    "name" : "Tanmay",
    "Maths": 45,
    "Science": 96,
    "Social": 75
}
Student_2 = {
    "name" : "Dheeraj",
    "Maths": 74,
    "Science": 100,
    "Social":83
}
Student_3 = {
    "name" :"Sooraj",
    "Maths":98,
    "Science": 25,
    "Social": 62
}
Student_list = [Student_1,Student_2,Student_3]
highest_score_in_social = 0
highest_score_in_social_Name = " "
for student in Student_list:
    if (student.get("Social") > highest_score_in_social):
        highest_score_in_social = student.get ("Social")
        highest_score_in_social_Name = student.get("name")

print(f"The highest scorer in social is {highest_score_in_social} by {highest_score_in_social_Name}")