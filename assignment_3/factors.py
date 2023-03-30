print("please enter a positive integer:")
num = int(input())
divisor = 0
print("The factors of", num, "are:")
for i in range(1, num+1):
    divisor += 1
    if num % divisor == 0:
        fac_num = divisor
        print(fac_num)



