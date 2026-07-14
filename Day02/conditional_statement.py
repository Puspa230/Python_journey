user_input = input("Enter your Score: ")
score = int(user_input)

if score >= 90:
    print("GRADE A")
elif score >=50:
    print("GRADE B")
else: 
    print("FAIL")