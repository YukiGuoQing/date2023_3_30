print("please enter a word: ")
user_input = input()
num = 0
for i in user_input:
    num += 1
if num % 2 == 0:
    print("even")
else:
    print("odd")
print("num_value", num)
