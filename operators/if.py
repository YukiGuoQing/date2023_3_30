#num = int(input())
#if num % 2 == 0:
#    print("num is even")
#else:
#    print("num is odd")

num = int(input())

fact_even = num % 2 == 0
fact_big = num >= 100
if fact_even and fact_big:
    print("the input number is even and great")

print("please type the score:")
score = int(input())
if score >= 90:
    grade = "S"
else:
    if score >= 80:
        grade = "A"
    else:
        if score >= 70:
            grade = "B"
        else:
            if score >= 60:
                grade = "C"
            else:
                grade = "D"

print("the grade is", grade)

print("please type the score:")
score = int(input())
if score >= 90:
    grade = "S"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"

print("the grade is", grade)