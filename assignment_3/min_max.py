print("how man integers would you like to enter?")
times = int(input())
print("please enter", times, "integers")
for i in range(1, times+1):
    user_num = int(input())
    if i == 1:
        max_num = user_num
        min_num = user_num
    if min_num >= user_num:
        min_num = user_num
    if max_num <= user_num:
        max_num = user_num
print("min:", min_num)
print("max:", max_num)




