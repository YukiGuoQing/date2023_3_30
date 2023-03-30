num = int(input())
if num >= 50 and num <= 100:
    print("in range")
else:
    print( "out of range")

num = int(input())
if num < 10:
    size = "small"
elif num >= 10 and num < 50:
    size = "medium"
else:
    size = "large"
print(size)

num = int(input())
if num == 1:
    letter = "one"
elif num == 2:
    letter = "two"
elif num == 3:
    letter ="three"
elif num == 4:
    letter = "four"
elif num == 5:
    letter = "five"
else:
    letter = "input not recognized"
print(letter)

