print("Enter the integer for the player to guess.")
num = int(input())
print("Enter your guess.")
try_num = "0"
times = 0
while try_num != num:
    try_num = int(input())
    if try_num > num:
        print("Too high - try again:")
    if try_num < num:
        print("Too low - try again:")
    times += 1
if times == 1:
    print("You guessed it in", times, "try")
else:
    print("You guessed it in", times, "tries")
