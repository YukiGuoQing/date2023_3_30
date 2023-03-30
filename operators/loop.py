num = 0
while num <= 9:
    num += 1
    print("hi")


word = "apple"
for letter in word:
    print(letter)

for num in range(1,11):
    print(num)

for num in range(1,15,3):
    print(num)
for num in range(37,5,-4):
    print(num)

for num in range(1,20):
    if(num == 16):
        break
    print(num)

total_num_letters = 0
print("Please enter the names of your three favorite animals.")
for val in range (1,4):
    animal = input()
    for letter in animal:
        total_num_letters += 1
print("Those names contained a total of",total_num_letters,"characters")